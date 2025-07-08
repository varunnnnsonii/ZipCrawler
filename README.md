
# 🗂️ ZipStructure – Selective Image Extractor & Folder Tree Viewer 📦🖼️

**ZipStructure** is a utility tool designed to:
1. ✅ **Extract specific images** from deeply nested folders inside ZIP archives.
2. 🌳 **Visualize the folder hierarchy** of ZIP files in a clean, tree-like format.

Perfect for quickly working with **datasets, archives, or AI training data** without extracting the entire ZIP contents!

---

## 🧾 Features

### 🖼️ Selective Image Extraction
Extract specific image files from a large ZIP without decompressing the whole archive.

Example:
```python
processed_dataset_zip/processed_dataset/image_gan_in_final/99.png
→ saved as → input.png
````

```python
processed_dataset_zip/processed_dataset/image_gan_out_final/99.png
→ saved as → output.png
```

---

### 🌳 Folder Tree Visualizer

View all folders inside a ZIP file in a clean, indented tree format — skips files and shows **only folders**, even nested ones.

Example output:

```
└── processed_dataset_zip
    └── processed_dataset
        └── image_gan_in_final
        └── image_gan_out_final
```

---

## 📂 Project Structure

```
ZipStructure/
├── zippicextractor.py       # Extracts specific images from a ZIP file
├── zipfoldertree.py         # Displays only folders in ZIP (tree-like)
├── archive.zip              # (your ZIP file goes here)
└── README.md                # You're reading it!
```

---

## 🔧 Requirements

* Python 3.6+
* Standard libraries only:

  * `zipfile`
  * `shutil`
  * `pathlib`

No extra installation needed! ✅

---

## 🚀 How to Use

### 📥 1. Extract Specific Images from ZIP

Edit `zippicextractor.py`:

```python
zip_path = "/path/to/archive.zip"
input_image = "path/in/zip/to/image.png"
output_image = "path/in/zip/to/image.png"
```

Then run:

```bash
python3 zippicextractor.py
```

Output:

```
✅ Saved: /your/path/input.png
✅ Saved: /your/path/output.png
```

---

### 🌳 2. Show Folder Tree from ZIP

Edit `zipfoldertree.py`:

```python
zip_path = "your_zip_file.zip"
```

Run:

```bash
python3 zipfoldertree.py
```

Output:

```
└── folder1
    └── subfolderA
    └── subfolderB
```

---

## ✅ Use Cases

* 📁 Working with large dataset ZIPs
* 🎨 Selective extraction for image/GAN projects
* 🧠 Organizing folders for deep learning pipelines
* 🔍 Exploring ZIP structure before full extraction

---

## 👨‍💻 Author

Created with ❤️ by [Varun Soni](https://github.com/varunnnnsonii)
If you find this helpful, feel free to ⭐ the repo!

---

## 🧠 Future Ideas

* ⬇️ Add support to extract entire folders
* 🔍 Search for files matching a pattern (e.g., `*.jpg`)
* 💻 Build a simple GUI with Tkinter or PyQt

---

## 📬 Feedback

Got ideas or issues? Open an [issue](https://github.com/varunnnnsonii/ZipStructure/issues) or reach out directly!

---

````

---

### ✅ Next Steps:

1. Save this as `README.md` inside your `ZipStructure` project.
2. Run:
```bash
git add README.md
git commit -m "📦 Add README explaining ZIP extraction and tree viewer"
git push origin main
````

