# Git & GitHub Practice: Expense Tracker

You'll build a small Python expense tracker. The coding is only half of the work.
The other half is doing every step the way a real developer would, with git and GitHub.

**Files you start with**
- `expense_tracker.py`: the app, with functions marked `TODO`
- `test_expense_tracker.py`: tests that check your work (`python -m unittest -v`)
- `ASSIGNMENT.md`: this file

**Rules**
- Type every git command yourself. Don't copy/paste whole blocks. Typing them is how you learn them.
- Run `git status` **constantly**: before and after almost every command. It's your best friend.
- If you're stuck, run `git <command> --help` or ask me. Don't just google and paste.
- Each part ends with **Check yourself** questions. Answer them out loud or in a notes file before you move on.

---

## Part 0: Setup (one time only)

1. Make a GitHub account at github.com if you don't have one.
2. Tell git who you are (this is what appears on your commits):
   ```
   git config --global user.name "Your Name"
   git config --global user.email "the-email-you-used-on-github@example.com"
   ```
   Check it with `git config --global --list`.
3. ⚠️ **Heads-up about your computer:** your whole user folder (`C:\Users\zyiki`) is
   *already* a git repository (someone ran `git init` there at some point). That's why
   `git status` in random folders shows a giant list of untracked files.
   - Open a terminal in this practice folder and run `git rev-parse --show-toplevel`. It prints `C:/Users/zyiki`. That's the repo you're "inside" right now.
   - When you `git init` in Part 1, you'll create a new, separate repo just for this folder, and git will use that one instead. Run the same command again after Part 1 and see what changes.
   - Later, you might decide to delete `C:\Users\zyiki\.git` (only that hidden folder, nothing else!) if you never meant to have it. Ask me before doing that.

**Check yourself:** What's the difference between git and GitHub?

---

## Part 1: Your first local repo

Do all of this in the `Github practice` folder.

1. Turn the folder into a repo: `git init`
2. Run `git status`. What does it say about your 3 files?
3. Rename the default branch to `main` (GitHub's default): `git branch -M main`
4. Create a file named `.gitignore` containing:
   ```
   __pycache__/
   expenses.json
   ```
   (`expenses.json` is your personal data. It should never go on GitHub.)
5. Stage **only** `.gitignore` and commit it:
   `git add .gitignore` → `git status` → `git commit -m "Add .gitignore"`
6. Stage and commit the other files in a **second** commit, with a good message.
7. Run `git log` and then `git log --oneline`.

**Check yourself:**
- What are the three "places" a change can be? (Hint: working directory, staging area, ...?)
- Why did we make two commits instead of one?
- What does a good commit message look like? (Short, present tense, says *what* and *why*.)

---

## Part 2: Put it on GitHub

1. On github.com, create a **new empty repository** called `expense-tracker`.
   Do **not** tick "Add a README" (your repo already has history, so keep GitHub's side empty).
2. GitHub shows you commands. Read them first, then connect your local repo:
   ```
   git remote add origin https://github.com/<your-username>/expense-tracker.git
   git remote -v
   git push -u origin main
   ```
   (A browser login window may pop up the first time. That's normal.)
3. Refresh the GitHub page. Your files and both commits should be there.
   Is `expenses.json` or `__pycache__` there? (It shouldn't be.)

**Check yourself:**
- What is `origin`?
- What does `-u` do, and why don't you need it next time?

---

## Part 3: Feature branch + Pull Request

Never work directly on `main`. Every feature gets its own branch.

1. Create and switch to a branch: `git switch -c feature/totals`
   Run `git branch` to see where you are.
2. Implement `make_expense`. Run the tests: `python -m unittest -v`
   (Lots of tests will fail. Only the `TestMakeExpense` ones need to pass for now.)
3. **Commit.** Just this one function.
4. Implement `total`. Test. **Commit.**
5. Implement `total_by_category`. Test. **Commit.**
   You should now have 3 small commits. Check with `git log --oneline`.
6. Before you commit, look at your changes with `git diff` (unstaged) and
   `git diff --staged` (staged). Get in the habit.
7. Push the branch: `git push -u origin feature/totals`
8. On GitHub, open a **Pull Request** from `feature/totals` → `main`.
   Write a description: what you did and how you tested it.
9. Look at the "Files changed" tab. Leave a comment on one of your own lines, like a reviewer would.
10. Click **Merge pull request**. Then click **Delete branch** on GitHub.
11. Back on your computer:
    ```
    git switch main
    git pull
    git branch -d feature/totals
    ```

**Check yourself:**
- After step 10, why didn't your local `main` have the new code until you ran `git pull`?
- What's the difference between `git branch -d` and `git branch -D`?

---

## Part 4: Issues & bug fixing

`most_expensive` has a bug. Run the app (`python expense_tracker.py`), pick option **4**
before adding anything, and watch it crash. (Options 3 and 5 will also crash until Parts 3 and 5 are done, so test with 4.)

1. On GitHub, go to the **Issues** tab and open a new issue:
   - Title: `most_expensive crashes when there are no expenses`
   - Body: steps to reproduce, what you expected, what happened (paste the error).
   - Note the issue number (probably `#1`... or `#2` because PRs share numbering!).
2. Make a branch for the fix: `git switch -c fix/empty-most-expensive`
3. Fix it so an empty list returns `None`. Run the tests.
4. Commit with a message that mentions the issue, e.g. `Fix crash in most_expensive on empty list (fixes #N)`
5. Push, open a PR, and in the PR description write `Fixes #N`.
6. Merge the PR. Go look at the issue. What happened to it?
7. Sync your local main again (`switch`, `pull`, delete branch).

**Check yourself:** Why is it useful to link commits/PRs to issues?

---

## Part 5: Make a merge conflict ON PURPOSE

Conflicts scare people. Let's make one so it stops being scary.

1. From an up-to-date `main`, make branch **A**: `git switch -c feature/save-load`
   - Implement `save_expenses` and `load_expenses` (use the `json` module; `os.path.exists` helps).
   - **Also** change the menu title line to `print("=== My Expense Tracker ===")`
   - Commit.
2. Go back to main: `git switch main`. Notice your save/load code "disappears". It's safe on the other branch!
3. Make branch **B** from main: `git switch -c feature/rename-title`
   - Change the **same** title line to `print("=== Money Log ===")`
   - Commit.
4. Merge B into main locally:
   ```
   git switch main
   git merge feature/rename-title
   ```
   (No conflict. This is a "fast-forward". Look up what that means.)
5. Now merge A: `git merge feature/save-load` 💥 **CONFLICT**
6. Run `git status`. Open the file and find the `<<<<<<<`, `=======`, `>>>>>>>` markers.
   Pick a final title (or combine them), delete the markers, save.
7. `git add expense_tracker.py` then `git commit` (git writes a merge message for you).
8. Run all tests. **Everything should pass now.** Push main.
9. `git log --oneline --graph --all` and look at the shape of your history.

**Check yourself:**
- Why did step 4 not conflict but step 5 did?
- What would `git merge --abort` have done at step 5?

---

## Part 6: Undoing things

Practice the "oh no" commands on purpose, in a safe place.

1. **Throw away an unsaved edit:** delete a random line in `expense_tracker.py`, save,
   then get it back with `git restore expense_tracker.py`.
2. **Unstage something:** edit a file, `git add` it, then undo the add with
   `git restore --staged <file>`. (The edit itself stays.)
3. **Fix your last commit message:** make a small commit with a typo in the message,
   then `git commit --amend -m "Better message"`. (Only do this before pushing!)
4. **Undo a pushed commit safely:** make a deliberately bad commit (e.g. delete the
   `total` function), push it, and watch the tests fail. Then undo it with
   `git revert <commit-hash>` and push again. Look at `git log`. Is the bad commit gone, or still there?
5. **Shelve work temporarily:** start editing something, then run `git stash`.
   `git status` is clean! Bring it back with `git stash pop`.

**Check yourself:**
- Why is `git revert` safe for pushed commits, but `git reset --hard` + force-push is dangerous?
- When would you use `git stash` in real life?

---

## Part 7: Changes from "someone else" + release

1. On GitHub, edit `ASSIGNMENT.md` (or add a `README.md`) **directly in the browser** and commit there.
   This simulates a teammate pushing work.
2. On your computer, **without pulling first**, make a commit and try `git push`. It gets rejected. Read the message.
3. Fix it with `git pull`, then push again.
4. Write a proper `README.md`: what the app does, how to run it, how to run the tests. Commit & push.
5. Tag your finished version:
   ```
   git tag -a v1.0 -m "First complete version"
   git push origin v1.0
   ```
6. On GitHub, go to **Releases** → **Draft a new release** → choose `v1.0` → publish it.

**Check yourself:** What does `git pull` actually do? (Hint: it's two commands in one.)

---

## Done? 🎉

When you're finished, your GitHub repo should have:
- [ ] At least 3 merged Pull Requests
- [ ] 1 closed issue (closed automatically by a PR)
- [ ] A merge commit from a resolved conflict
- [ ] A revert commit
- [ ] A `README.md`
- [ ] A `v1.0` tag and release
- [ ] All tests passing: `python -m unittest -v`

Show me your `git log --oneline --graph --all` output and I'll review your history.

### Bonus challenges
- Add a "delete expense" menu option using the full branch → PR → merge flow.
- Fork a classmate's repo, make a change, and send them a PR from your fork.
- Try `git rebase main` instead of merging on a feature branch. What's different about the history?
- Install the GitHub CLI (`gh`) and open a PR from the terminal with `gh pr create`.
