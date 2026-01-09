# main.py

from parser import extract_resume_text
from skill_extractor import extract_skills
from evaluator import evaluate_role
from scorer import calculate_ats_score
from job_role import job_roles_skills

from llm_skill_suggester import suggest_additional_skills
from llm_explainer import explain_result
from llm_roadmap import generate_roadmap

from semantic_similarity import compute_similarity
from job_descriptions import job_descriptions


def main():
    print("=" * 60)
    print("📄 ATS RESUME EVALUATION SYSTEM")
    print("=" * 60)

    # --------------------------------------------------
    # 1. Read & parse resume
    # --------------------------------------------------
    resume_path = "core/fake_resume.txt"
    resume_text = extract_resume_text(resume_path)

    print("\n[1] Resume loaded successfully")
    print(f"    File: {resume_path}")

    # --------------------------------------------------
    # 2. Skill extraction
    # --------------------------------------------------
    rule_based_skills = extract_skills(resume_text)
    llm_suggested_skills = suggest_additional_skills(resume_text)

    known_skills = rule_based_skills | llm_suggested_skills

    print("\n[2] Skill Extraction")
    print("    Rule-based skills:")
    print("     ", sorted(rule_based_skills))

    print("    LLM-suggested skills (extra):")
    print("     ", sorted(llm_suggested_skills - rule_based_skills))

    print("    Final known skills:")
    print("     ", sorted(known_skills))

    # --------------------------------------------------
    # 3. Evaluate against all job roles
    # --------------------------------------------------
    results = []

    for role_name, role_data in job_roles_skills.items():
        evaluation = evaluate_role(role_name, role_data, known_skills)

        job_desc = job_descriptions.get(role_name, "")
        similarity = compute_similarity(resume_text, job_desc)

        evaluation["semantic_similarity"] = similarity

        final = calculate_ats_score(evaluation, resume_text, known_skills)
        results.append(final)


    if not results:
        print("\n❌ No roles evaluated.")
        return

    # Sort by ATS score (descending)
    results.sort(key=lambda x: x["ats_score"], reverse=True)

    # --------------------------------------------------
    # 4. Show top matching roles
    # --------------------------------------------------
    print("\n[3] Top Matching Roles")
    print("-" * 60)

    for r in results[:3]:
        print(f"Role: {r['role']}")
        print(f"ATS Score: {r['ats_score']}%")
        print(f"Fit Level: {r['fit']}")
        print(f"ML Pass Probability: {r['ml_pass_probability']}%")

        print("Missing Core Skills:")
        for skill, _ in r["missing_core"]:
            print(f" - {skill}")

        print("-" * 60)

    # --------------------------------------------------
    # 5. LLM Explanation & Roadmap (TOP ROLE ONLY)
    # --------------------------------------------------
    top_role = results[0]

    print("\n[4] AI Explanation (Why this result?)")
    print("-" * 60)
    print(explain_result(top_role))

    print("\n[5] Personalized Career Roadmap")
    print("-" * 60)

    missing_skills = [skill for skill, _ in top_role["missing_core"]]
    print(generate_roadmap(top_role["role"], missing_skills))

    print("\n✅ Evaluation complete.")
    print("=" * 60)

    print(f"Semantic Match Score: {r.get('semantic_similarity', 0)}")


if __name__ == "__main__":
    main()
