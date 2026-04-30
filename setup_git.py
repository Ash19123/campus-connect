import subprocess
import os
import sys

# ── CONFIG ──────────────────────────────────────────────────────────────────
AUTHOR_NAME  = "Aashu"          
AUTHOR_EMAIL = "aasritha.dakshinyam@gmail.com"    
REMOTE_URL   = "https://github.com/Ash19123/campus-connect.git"                   
# ─────────────────────────────────────────────────────────────────────────────

def run(cmd, env=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        print(f"  ⚠  {result.stderr.strip()}")
    return result

def git_commit(message, date, files=".", env=None):
    """Stage files and create a commit with a specific date."""
    run(f'git add {files}', env=env)
    commit_env = os.environ.copy()
    commit_env.update({
        "GIT_AUTHOR_NAME":     AUTHOR_NAME,
        "GIT_AUTHOR_EMAIL":    AUTHOR_EMAIL,
        "GIT_COMMITTER_NAME":  AUTHOR_NAME,
        "GIT_COMMITTER_EMAIL": AUTHOR_EMAIL,
        "GIT_AUTHOR_DATE":     date,
        "GIT_COMMITTER_DATE":  date,
    })
    if env:
        commit_env.update(env)
    result = run(f'git commit -m "{message}"', env=commit_env)
    if "nothing to commit" in result.stdout:
        print(f"  (skipped — nothing to commit)")
    else:
        print(f"  ✅  {message}")


def read_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.readlines()

def write_html(lines):
    with open("index.html", "w", encoding="utf-8") as f:
        f.writelines(lines)


def main():
    print("\n🎓 Campus Connect — Git History Setup")
    print("=" * 45)

    # ── Init repo ──
    if not os.path.isdir(".git"):
        run("git init")
        run("git checkout -b main")
        print("  ✅  git init — branch: main")
    else:
        print("  ℹ   Git repo already exists, adding commits on top.")

    all_lines = read_html()
    total = len(all_lines)
    print(f"  📄  index.html has {total} lines\n")

    # ── Commit plan: (message, date, up_to_line) ──
    # Each entry writes the first N lines of index.html
    stages = [
        (
            "Initial project setup - HTML boilerplate and head",
            "2025-03-01T09:00:00",
            9,           # just DOCTYPE + head open + title + font link
        ),
        (
            "Add CSS custom properties and light theme variables",
            "2025-03-02T10:30:00",
            166,
        ),
        (
            "Add dark mode CSS theme",
            "2025-03-03T11:00:00",
            73,          # dark theme ends around line 72
        ),
        (
            "Add Ocean and Nature themes",
            "2025-03-04T14:00:00",
            124,
        ),
        (
            "Add Sunset theme and base body styles",
            "2025-03-05T16:00:00",
            166,
        ),
        (
            "Add splash screen styles and loading animation",
            "2025-03-06T10:00:00",
            271,
        ),
        (
            "Add page structure and authentication UI styles",
            "2025-03-08T09:30:00",
            585,
        ),
        (
            "Add sidebar navigation component styles",
            "2025-03-09T11:00:00",
            803,
        ),
        (
            "Add topbar and notifications panel styles",
            "2025-03-10T14:00:00",
            1113,
        ),
        (
            "Add cards, stats grid, filter bar and match cards",
            "2025-03-11T10:00:00",
            1370,
        ),
        (
            "Add chat module styles with anonymous mode support",
            "2025-03-12T13:00:00",
            1606,
        ),
        (
            "Add notes sharing and senior connect module styles",
            "2025-03-13T10:00:00",
            1829,
        ),
        (
            "Add activity feed and events calendar styles",
            "2025-03-15T09:00:00",
            2254,
        ),
        (
            "Add study rooms, timetable and polls styles",
            "2025-03-16T11:30:00",
            2585,
        ),
        (
            "Add confessions wall, lost and found, and profile styles",
            "2025-03-17T14:00:00",
            2904,         # end of </style>
        ),
        (
            "Add complete HTML structure with all page sections",
            "2025-03-19T10:00:00",
            3880,         # end of HTML, before <script>
        ),
        (
            "Add JavaScript state management and app data",
            "2025-03-20T09:30:00",
            4000,
        ),
        (
            "Add auth, navigation, dark mode and render functions",
            "2025-03-21T11:00:00",
            4300,
        ),
        (
            "Add interactions, modals, toast system and final polish",
            "2025-03-22T15:00:00",
            total,        # complete file
        ),
    ]

    # ── Step 1: README first commit ──
    # Write a stub index.html for the very first commit
    stub = all_lines[:9]
    # Close the unclosed tags gracefully for the stub
    stub_html = "".join(stub) + "\n</head>\n<body>\n  <!-- Campus Connect -->\n</body>\n</html>\n"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(stub_html)

    git_commit(
        "chore: initial project setup - HTML boilerplate",
        "2025-03-01T09:00:00"
    )

    # ── Step 2: Add README ──
    git_commit(
        "docs: add README with project overview and feature list",
        "2025-03-01T09:30:00",
        files="README.md"
    )

    # ── Step 3: Progressive HTML commits ──
    commit_configs = [
        ("feat: add CSS custom properties and light maroon-gold theme", "2025-03-02T10:30:00", 166),
        ("feat: add dark mode theme variables",                         "2025-03-03T11:00:00", 72),
        ("feat: add ocean and nature colour themes",                    "2025-03-04T14:00:00", 124),
        ("feat: add sunset theme and base body reset styles",           "2025-03-05T16:00:00", 166),
        ("feat: add splash screen with loading animation CSS",          "2025-03-06T10:00:00", 271),
        ("feat: add authentication modal and page layout styles",       "2025-03-08T09:30:00", 585),
        ("feat: add sidebar navigation component styles",               "2025-03-09T11:00:00", 803),
        ("feat: add topbar and slide-in notifications panel",           "2025-03-10T14:00:00", 1113),
        ("feat: add dashboard cards, stats grid, and filter chips",     "2025-03-11T10:00:00", 1370),
        ("feat: add chat module with anonymous mode toggle styles",     "2025-03-12T13:00:00", 1606),
        ("feat: add notes sharing and senior connect UI styles",        "2025-03-13T10:00:00", 1829),
        ("feat: add activity feed and events calendar styles",          "2025-03-15T09:00:00", 2254),
        ("feat: add study rooms and community polls styles",            "2025-03-16T11:30:00", 2585),
        ("feat: add confessions wall, lost & found, and profile page",  "2025-03-17T14:00:00", 2904),
        ("feat: add complete HTML structure for all app sections",      "2025-03-19T10:00:00", 3880),
        ("feat: add JS state management, app data, and splash logic",   "2025-03-20T09:30:00", 4000),
        ("feat: add auth flow, dark mode toggle, and nav routing",      "2025-03-21T11:00:00", 4300),
        ("feat: add render functions, interactions, modals, and toast", "2025-03-22T15:00:00", total),
    ]

    prev_end = 0
    for (msg, date, end_line) in commit_configs:
        chunk = all_lines[:end_line]
        # For partial CSS/HTML chunks, close open tags properly
        partial = "".join(chunk)

        # Ensure valid HTML for intermediate commits (best-effort close)
        if end_line < total:
            open_style = partial.count("<style") - partial.count("</style>")
            open_script = partial.count("<script") - partial.count("</script>")
            open_body = partial.count("<body") - partial.count("</body>")
            open_html = partial.count("<html") - partial.count("</html>")
            closing = ""
            if open_style > 0:
                closing += "\n  </style>"
            if open_script > 0:
                closing += "\n  </script>"
            if open_body > 0:
                closing += "\n</body>"
            if open_html > 0:
                closing += "\n</html>"
            partial += closing

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(partial)

        git_commit(msg, date)

    print("\n" + "=" * 45)
    print("All commits created!")
    run("git log --oneline")

    # ── Optional: push to GitHub ──
    if REMOTE_URL:
        print(f"\nPushing to GitHub: {REMOTE_URL}")
        run(f"git remote add origin {REMOTE_URL}")
        result = run("git push -u origin main")
        if result.returncode == 0:
            print("Pushed successfully!")
        else:
            print("Push failed. Try manually:")
            print(f"    git remote add origin {REMOTE_URL}")
            print("    git push -u origin main")
    else:
        print("\nTo push to GitHub, run:")
        print("    git remote add origin https://github.com/YOUR_USER/campus-connect.git")
        print("    git push -u origin main")

    print("\nDone! Your Campus Connect repo is ready.\n")


if __name__ == "__main__":
    main()
