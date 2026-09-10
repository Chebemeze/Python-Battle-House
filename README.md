# 🐍 Python Battle House

> **A repository of Python challenges and exploratory tasks — for fun and learning.**

![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Challenges](https://img.shields.io/badge/challenges-59%20scripts-green?style=flat-square)
![Pytest](https://img.shields.io/badge/tests-pytest-0A9EDC?style=flat-square)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)

Welcome to the **Battle House** — my training ground for Python. Every challenge that steps into this ring gets broken down, solved, and studied: conditionals drills, sorting algorithms, dict wrangling, asyncio coroutines, live API calls, and free-form "what happens if…?" experiments. The goal isn't production-perfect code; it's **reps, curiosity, and notes about what each fight taught me**.

---

## 🗂️ Repository layout

```text
Python-Battle-House/
├── README.md
├── .gitignore
└── python-lessons/
    ├── 01-basics-and-control-flow/   # conditionals, loops, small games
    ├── 02-functions-and-python-features/  # closures, lambdas, decorators, generators
    ├── 03-errors-and-debugging/      # try/except, match/case hints, code tracing
    ├── 04-strings-and-text/          # text munging and validation
    ├── 05-dicts-and-grouping/        # dictionaries, tallies, grouping, aggregations
    ├── 06-numbers-and-logic/         # money math, max/min, parity
    ├── 07-algorithms-and-data-structures/  # sorts, searches, stacks, linked lists
    ├── 08-concurrency/               # threads, processes, asyncio coroutines
    ├── 09-files-and-apis/            # CSV export, HTTP calls, ISS passes
    ├── playground/                   # scratch files (HTML/JS/Python experiments)
    └── pytest_examples/              # module + test pairs for pytest practice
```

Every challenge lives in **its own folder**, grouped by topic. Folder names match the script names, so anything you see in the index below is one hop away.

## 📜 Challenge index

### 01 · Basics & control flow — `python-lessons/01-basics-and-control-flow/`

| Challenge | What it does |
|-----------|--------------|
| [`age_category`](python-lessons/01-basics-and-control-flow/age_category/age_category.py) | Classify an age into life-stage bands, with an empty-input guard |
| [`cinema_ticket_pricing`](python-lessons/01-basics-and-control-flow/cinema_ticket_pricing/cinema_ticket_pricing.py) | Ticket price from age + weekday/weekend |
| [`day_5`](python-lessons/01-basics-and-control-flow/day_5/day_5.py) | Hospital triage: which patient gets treated first |
| [`day_6`](python-lessons/01-basics-and-control-flow/day_6/day_6.py) | Supermarket discount from basket total, loyalty & promo day |
| [`delivery`](python-lessons/01-basics-and-control-flow/delivery/delivery.py) | Delivery fee from order total, distance and membership |
| [`gate_pass`](python-lessons/01-basics-and-control-flow/gate_pass/gate_pass.py) | Venue access rules: age, ID, banned list |
| [`guessing_game`](python-lessons/01-basics-and-control-flow/guessing_game/guessing_game.py) | `while`-loop guess-the-number game |
| [`password_simulator`](python-lessons/01-basics-and-control-flow/password_simulator/password_simulator.py) | Login simulator with a 4-attempt lockout |
| [`triangle_pattern`](python-lessons/01-basics-and-control-flow/triangle_pattern/triangle_pattern.py) | Build a triangle pattern with nested loops |
| [`voter_elligibility`](python-lessons/01-basics-and-control-flow/voter_elligibility/voter_elligibility.py) | Vote eligibility with input validation |

### 02 · Functions & Python features — `python-lessons/02-functions-and-python-features/`

| Challenge | What it does |
|-----------|--------------|
| [`decorators`](python-lessons/02-functions-and-python-features/decorators/decorators.py) | Decorators from manual wrapping up to `@` syntax, with doctests |
| [`function_play`](python-lessons/02-functions-and-python-features/function_play/function_play.py) | Nested functions & closures in seven lines |
| [`lambda`](python-lessons/02-functions-and-python-features/lambda/lambda.py) | `def` vs `lambda`, side by side |
| [`iterator`](python-lessons/02-functions-and-python-features/iterator/iterator.py) | Iterable vs iterator: inspect `__iter__` / `__next__` live |
| [`yield_generator`](python-lessons/02-functions-and-python-features/yield_generator/yield_generator.py) | Generators & `yield` vs building plain lists |

### 03 · Errors & debugging — `python-lessons/03-errors-and-debugging/`

| Challenge | What it does |
|-----------|--------------|
| [`error_hint`](python-lessons/03-errors-and-debugging/error_hint/error_hint.py) | `match`/`case` that returns a fix-it hint per exception type |
| [`score_summary`](python-lessons/03-errors-and-debugging/score_summary/score_summary.py) | Safe int parsing with `try/except ValueError` |
| [`trace_error`](python-lessons/03-errors-and-debugging/trace_error/trace_error.py) | Trace a snippet in your head and predict its output |

### 04 · Strings & text — `python-lessons/04-strings-and-text/`

| Challenge | What it does |
|-----------|--------------|
| [`capitalize_special_words`](python-lessons/04-strings-and-text/capitalize_special_words/capitalize_special_words.py) | Title case that spares connector words (a, of, the…) |
| [`count_vowel`](python-lessons/04-strings-and-text/count_vowel/count_vowel.py) | Case-insensitive vowel counter |
| [`initial_badge`](python-lessons/04-strings-and-text/initial_badge/initial_badge.py) | Full name → initials badge |
| [`isbn_10`](python-lessons/04-strings-and-text/isbn_10/isbn_10.py) | Validate an ISBN-10 read from stdin |
| [`palindrom`](python-lessons/04-strings-and-text/palindrom/palindrom.py) | Manual palindrome check with cleaning & normalization |
| [`password_checker`](python-lessons/04-strings-and-text/password_checker/password_checker.py) | Rate password strength by length & character mix |
| [`slug-maker`](python-lessons/04-strings-and-text/slug-maker/slug-maker.py) | Turn a title into a URL slug |

### 05 · Dicts & grouping — `python-lessons/05-dicts-and-grouping/`

| Challenge | What it does |
|-----------|--------------|
| [`dictionary_copy`](python-lessons/05-dicts-and-grouping/dictionary_copy/dictionary_copy.py) | Aliasing vs `copy()`: why `=` is not a copy |
| [`duplicate_dict`](python-lessons/05-dicts-and-grouping/duplicate_dict/duplicate_dict.py) | Drop duplicate dict entries, keep the first |
| [`fav_color_survey`](python-lessons/05-dicts-and-grouping/fav_color_survey/fav_color_survey.py) | Tally survey responses with `dict.get` |
| [`group_by_students`](python-lessons/05-dicts-and-grouping/group_by_students/group_by_students.py) | Group students into letter-grade bands |
| [`longest_streak_tracker`](python-lessons/05-dicts-and-grouping/longest_streak_tracker/longest_streak_tracker.py) | Current & longest attendance streaks per student |
| [`restock_items`](python-lessons/05-dicts-and-grouping/restock_items/restock_items.py) | Flag stock that fell below minimum levels |
| [`roll_cleaner`](python-lessons/05-dicts-and-grouping/roll_cleaner/roll_cleaner.py) | De-duplicate a roll call: nested loops → sets |
| [`student_grade_lookup`](python-lessons/05-dicts-and-grouping/student_grade_lookup/student_grade_lookup.py) | Name → grade lookup over a list of records |
| [`sum_appearance`](python-lessons/05-dicts-and-grouping/sum_appearance/sum_appearance.py) | Aggregate quantities and appearance counts per item |
| [`total_score_finder`](python-lessons/05-dicts-and-grouping/total_score_finder/total_score_finder.py) | Accumulate per-player totals across rounds |
| [`word_grouping`](python-lessons/05-dicts-and-grouping/word_grouping/word_grouping.py) | Group words by length into a dict |

### 06 · Numbers & logic — `python-lessons/06-numbers-and-logic/`

| Challenge | What it does |
|-----------|--------------|
| [`basic_market_calculator`](python-lessons/06-numbers-and-logic/basic_market_calculator/basic_market_calculator.py) | Market receipt: rice, beans & garri breakdown |
| [`change_maker`](python-lessons/06-numbers-and-logic/change_maker/change_maker.py) | Compute change in coins; raises on underpayment |
| [`find_max`](python-lessons/06-numbers-and-logic/find_max/find_max.py) | Largest number, handling negative-start edge cases |
| [`second_largest_algo`](python-lessons/06-numbers-and-logic/second_largest_algo/second_largest_algo.py) | Second largest *distinct* value in a list |
| [`sum_of_even`](python-lessons/06-numbers-and-logic/sum_of_even/sum_of_even.py) | Sum of even numbers with a `None` guard |

### 07 · Algorithms & data structures — `python-lessons/07-algorithms-and-data-structures/`

| Challenge | What it does |
|-----------|--------------|
| [`binary_search_tree`](python-lessons/07-algorithms-and-data-structures/binary_search_tree/) | BST insert (`binary_insert.py`) + BST search (`binary_search.py`) — kept in one folder because search imports insert |
| [`bracket_checker`](python-lessons/07-algorithms-and-data-structures/bracket_checker/bracket_checker.py) | Balance `()`, `[]`, `{}` with a stack |
| [`insertion_sort`](python-lessons/07-algorithms-and-data-structures/insertion_sort/insertion_sort.py) | Insertion sort, swap logic commented line by line |
| [`linked_list`](python-lessons/07-algorithms-and-data-structures/linked_list/linked_list.py) | Nodes & pointers: a linked-list / FILO exploration |
| [`merge_sort`](python-lessons/07-algorithms-and-data-structures/merge_sort/merge_sort.py) | Merge two sorted halves, then full merge sort |
| [`quick_sort`](python-lessons/07-algorithms-and-data-structures/quick_sort/quick_sort.py) | Quicksort via pivot partition comprehensions |

### 08 · Concurrency — `python-lessons/08-concurrency/`

| Challenge | What it does |
|-----------|--------------|
| [`basic_multiprocess`](python-lessons/08-concurrency/basic_multiprocess/basic_multiprocess.py) | `multiprocessing` processes as a roaster-audit simulation |
| [`dividend_calculator`](python-lessons/08-concurrency/dividend_calculator/dividend_calculator.py) | `Pool.map` over a squares-sum workload |
| [`match_case`](python-lessons/08-concurrency/match_case/match_case.py) | Threaded locked-counter experiment (currently commented out) |
| [`multiple_coroutine`](python-lessons/08-concurrency/multiple_coroutine/multiple_coroutine.py) | asyncio coroutines querying IoT sensors concurrently |
| [`sensor_corountine`](python-lessons/08-concurrency/sensor_corountine/sensor_corountine.py) | A single-coroutine sensor status check |
| [`thread_pool`](python-lessons/08-concurrency/thread_pool/thread_pool.py) | `ThreadPoolExecutor` instead of manual threads |
| [`threaded`](python-lessons/08-concurrency/threaded/threaded.py) | Manual threads racing on a global counter |

### 09 · Files & APIs — `python-lessons/09-files-and-apis/`

| Challenge | What it does |
|-----------|--------------|
| [`callapi`](python-lessons/09-files-and-apis/callapi/callapi.py) | GET ISS pass times over Port Harcourt and save the JSON response (`library.json` kept alongside) |
| [`exporter`](python-lessons/09-files-and-apis/exporter/exporter.py) | Export a book list to CSV (`library_export.csv` sample kept alongside) |
| [`isspass`](python-lessons/09-files-and-apis/isspass/isspass.py) | Fetch & human-format the next five ISS passes for any location |

### 🧪 pytest practice — `python-lessons/pytest_examples/`

Four module + test pairs for pytest practice: `calculator`, `kiosk`, `weather`, `yield_cart`.

### 🎮 Playground — `python-lessons/playground/`

Scratch, not (yet) challenges: `home.html` (HTML skeleton), `start.js` (first React-style component), `test.py` (bracket-walker + `split()` experiments with commented API/datetime notes).

---

## 🏁 Getting started

Most challenges run on the **standard library alone**:

```bash
git clone https://github.com/Chebemeze/Python-Battle-House.git
cd Python-Battle-House

# run any challenge from its own folder
cd python-lessons/04-strings-and-text/palindrom
python3 palindrom.py

# run the pytest practice suite (from the repo root)
python3 -m pytest python-lessons/pytest_examples -v
```

Challenges that talk to the network (`callapi`, `isspass`) need `requests`:

```bash
pip install requests
```

> **Note:** `binary_search.py` imports its sibling `binary_insert.py`, so run it from inside its own folder (or with that folder on `PYTHONPATH`) — exactly as organized here.

## 🧭 House rules

1. **One challenge, one folder.** New challenge? New folder under the matching topic.
2. **Brute force → optimize → refactor.** A working ugly solution beats a beautiful missing one.
3. **History is a training log.** Small, focused commits per challenge.
4. **Coupled files stay together.** If script A imports script B or writes a data file, they share a folder.
5. **Have fun.** It's a battle *house*, not a battle *office*.

## 🗺️ Roadmap

- [ ] `challenge.md` problem statements inside each challenge folder
- [ ] pytest coverage for every solved challenge
- [ ] Difficulty tags (🟢🔴) in the index
- [ ] A "sparring partners" list: classics worth re-solving from scratch

## 🤝 Contributing

Personal learning repo, but sparring is welcome. Spotted a bug, a cleaner approach, or a fun challenge idea? Open an **issue** or send a **pull request** — bonus points if your PR makes a solution faster *and* more readable.

## 📬 Contact

**Eze Chukwuchebem Ebenezer** — [@Chebemeze](https://github.com/Chebemeze)
· [LinkedIn](https://www.linkedin.com/in/eze-chukwuchebem-ebenezer/)
· [X @Itz_eben](https://x.com/Itz_eben)

---

*Step into the house. Bring your syntax errors.* 🥊
