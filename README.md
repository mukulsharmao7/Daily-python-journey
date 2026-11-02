# ML Journey

My daily learning log on the way to becoming an AI/ML and Gen AI engineer.
I write the code myself, review it, and push it here every day.

**Goal:** AI/ML Engineer, Gen AI Engineer, Data Scientist.
**Student at:** Triple IT Bhopal.
**Status:** Day 9 in progress.

## What is inside

| Folder | Topic | What I practised |
|---|---|---|
| `day-1-lists` | Python lists and dictionaries | List comprehension, `max` with `key`, averages, edge cases like an empty list, basic web scraping with `requests` and `BeautifulSoup` |
| `day-2-json` | File handling and JSON | `with open()`, file modes, `json.dump` / `json.load`, `try/except FileNotFoundError`, save-load-analyze pipeline |
| `day-3-Api` | API calls | `requests.get`, `response.json()`, nested dictionaries, `raise_for_status()`, error handling, API-clean-save pipeline |
| `day-4-pandas` | Pandas basics | DataFrames, selecting columns, `iloc`, filtering, sorting, string methods, `to_csv` and `read_csv` |
| `day-6-TaskB` | Production Python | Type hints, input validation, `TypeError` vs `ValueError`, clean functions |
| `day7-TaskA` | Images as NumPy arrays | `cv2.imread`, shape and dtype, BGR vs RGB, color channels, `uint8` overflow and `np.clip` |
| `day8-TaskA` | Basic image operations | Grayscale, resize and interpolation, crop with slicing, flip |
| `day9-TaskA` | Intensity transformations | Image negative, log transform (work in progress) |

NumPy basics (arrays, indexing, slicing, views vs copies, boolean masking, `reshape`) and vectorization, broadcasting and statistics were covered in Days 5 and 6.

## Skills so far

- **Python:** functions, type hints, file handling, JSON, error handling, testing with `assert` and `pytest`
- **Data:** Pandas basics, NumPy arrays, broadcasting, `axis` operations
- **Image processing:** OpenCV, Matplotlib, grayscale, resizing, cropping, flipping, intensity transforms (following *Digital Image Processing* by Gonzalez and Woods)
- **Tools:** Jupyter Notebook, VS Code, Git and GitHub

## Things I learned the hard way

- `cv2.imread` does not raise an error for a wrong path. It returns `None`, so I always check `if img is None`.
- OpenCV reads images as BGR, Matplotlib expects RGB. I convert before `plt.imshow`.
- `uint8` wraps around (`250 + 10 = 4`). I convert to a bigger type, then `np.clip`, then back to `uint8`.
- Array slices are views, not copies. I use `.copy()` when I need to keep the original safe.
- `img.shape` is `(height, width)` but `cv2.resize` takes `(width, height)`.
- In tests, an error is the expected result. `assert False` after the call catches the case where no error was raised.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install numpy opencv-python matplotlib pandas requests beautifulsoup4 pytest jupyter
```

Notebooks use `plt.imshow()` to show images (not `cv2.imshow()`).

## Roadmap

1. Image processing with NumPy and OpenCV (histograms, spatial filtering, mini project)
2. Production Python (logging, testing, environments)
3. Web scraping and APIs (full jobs scraper)
4. Pandas EDA and SQL
5. Statistics and machine learning with scikit-learn
6. Deep learning with PyTorch
7. LLM APIs, embeddings and RAG
8. Agentic AI (tool calling, LangGraph)
9. Deployment (FastAPI, Docker) and a final portfolio

## Daily routine

One small task at a time, written by hand, reviewed, then pushed with a short commit message.