import streamlit as st
import tempfile
import os

from parser import extract_resume_text
from skill_extractor import extract_skills
from evaluator import evaluate_role
from scorer import calculate_ats_score
from job_role import job_roles_skills

from llm_explainer import explain_result
from semantic_similarity import compute_similarity
from job_descriptions import job_descriptions
from resume_validator import validate_resume
from roadmap_builder import build_resource_roadmap


# --------------------------------------------------
# App config
# --------------------------------------------------
st.set_page_config(page_title="ATS Resume Evaluation System", layout="centered")

st.markdown("## 🖥️ ATS Resume Evaluation System")
st.caption("Upload your resume and get AI-powered insights with career guidance.")


# --------------------------------------------------
# Session state
# --------------------------------------------------
for key in ["resume_text", "verified_skills", "results", "llm_cache"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "llm_cache" else {}


# --------------------------------------------------
# Upload resume
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"]
)

if uploaded_file and st.session_state.resume_text is None:
    with st.spinner("📄 Reading resume..."):
        suffix = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            path = tmp.name

        st.session_state.resume_text = extract_resume_text(path)
        os.remove(path)

        st.success("✅ Resume processed successfully!")


# --------------------------------------------------
# Validate resume
# --------------------------------------------------
if st.session_state.resume_text:
    validation = validate_resume(st.session_state.resume_text)

    if validation["confidence"] < 0.4:
        st.error("❌ This does not look like a resume.")
        st.stop()
    elif validation["confidence"] < 0.65:
        st.warning("⚠️ Resume structure is weak. Results may vary.")


# --------------------------------------------------
# Skill extraction
# --------------------------------------------------
if st.session_state.resume_text and st.session_state.verified_skills is None:
    with st.spinner("🧠 Extracting skills..."):
        st.session_state.verified_skills = extract_skills(
            st.session_state.resume_text
        )


# --------------------------------------------------
# Extracted skills (clean)



# --------------------------------------------------
# Role evaluation
# --------------------------------------------------
if st.session_state.results is None and st.session_state.verified_skills:
    with st.spinner("🔍 Evaluating job roles..."):
        results = []

        for role, data in job_roles_skills.items():
            evaluation = evaluate_role(
                role, data, st.session_state.verified_skills
            )

            jd = job_descriptions.get(role, "")
            evaluation["semantic_similarity"] = compute_similarity(
                st.session_state.resume_text, jd
            )

            final = calculate_ats_score(
                evaluation,
                st.session_state.resume_text,
                st.session_state.verified_skills
            )

            results.append(final)

        st.session_state.results = sorted(
            results, key=lambda x: x["ats_score"], reverse=True
        )


# --------------------------------------------------
# Top matching roles (CARD STYLE)
# --------------------------------------------------
if st.session_state.results:
    st.subheader("📊 Top Matching Roles")

    cols = st.columns(3)

    for col, r in zip(cols, st.session_state.results[:3]):
        with col:
            st.markdown(f"### {r['role']}")

            st.progress(min(r["ats_score"] / 100, 1.0))
            st.caption(f"ATS Score: **{r['ats_score']}%**")

            if r["fit"] == "Good Fit":
                st.success("Good Fit")
            else:
                st.warning("Needs Upskilling")


            if r["missing_core"]:
                for s, _ in r["missing_core"][:3]:
                    st.write("•", s)


# --------------------------------------------------
# AI Guidance (Optional)
# --------------------------------------------------
st.subheader("🎯 AI Guidance")

if st.session_state.results:
    role_names = [r["role"] for r in st.session_state.results[:5]]
    selected_role = st.selectbox("Choose a role:", role_names)

    selected = next(
        r for r in st.session_state.results if r["role"] == selected_role
    )
    missing = [s for s, _ in selected["missing_core"]]

    if st.button("🤖 Generate AI Explanation & Learning Plan"):
        with st.spinner("Thinking..."):
            explanation = explain_result(selected)
            roadmap = build_resource_roadmap(selected_role, missing) or []

            st.session_state.llm_cache[selected_role] = {
                "explanation": explanation,
                "resources": roadmap,
            }

    if selected_role in st.session_state.llm_cache:
        data = st.session_state.llm_cache[selected_role]

        with st.expander("💡 AI Explanation"):
            st.write(data["explanation"])

        st.subheader("📘 Personalized Career Roadmap")

        resources = data.get("resources", [])
        if not resources:
            st.success(
                "You already meet most core requirements for this role. "
                "Focus on projects, interview prep, and real-world applications."
            )
        else:
            for i, item in enumerate(resources, start=1):
                st.markdown(
                    f"### Month {i}: Learn {item.get('skill', 'Skill')}"
                )

                for r in item.get("resources", [])[:2]:
                    st.markdown(
                        f"- [{r.get('title', 'Untitled')}]({r.get('link', '#')}) "
                        f"— {r.get('platform', '')}<br/>"
                        f"<small>{r.get('reason', '')}</small>",
                        unsafe_allow_html=True
                    )

        # 👇 DISCLAIMER APPEARS LAST (after roadmap)
        st.info(
            "ℹ️ The explanation and roadmap above are generated using a "
            "logic-driven, rule-based approach to ensure transparency and reliability. "
            "The system architecture supports optional LLM integration when available."
        )
