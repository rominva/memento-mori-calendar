# 🕯️ Memento Mori Calendar

A simple Python command-line application that helps you keep your **Memento Mori** calendar up to date.

Instead of manually calculating your current week of life, this program tells you exactly **which row (year)** and **which week** to fill in on your printed Memento Mori calendar.

> *"It is not that we have a short time to live, but that we waste much of it."*  
> — Seneca

---

## 📖 What is Memento Mori?

*Memento Mori* is a Latin phrase meaning **"Remember that you must die."**

One popular visualization is the **Memento Mori Calendar**, where:

- Each **row** represents one year of life.
- Each **square** represents one week.
- Filling a square reminds us that every week is valuable and should be lived intentionally.

---

## ✨ Features

- Accepts a birth date in **YYYY-MM-DD** format.
- Calculates your **current calendar year**.
- Calculates how many **weeks have passed since your last birthday**.
- Displays a simple visual progress bar in the terminal.
- Handles invalid dates safely.
- Supports people born on **February 29**.

---

## 🖥️ Example
![Demo](https://github.com/rominva/memento-mori-calendar/blob/main/assets/memento_mori_demo.gif)

---

## ▶️ Usage

Run:

```bash
python memento_mori.py
```

Example:

```text
Date of Birth: 1998-10-05
```

---

## 📦 Requirements

- Python 3.10+
- colorama

Install manually:

```bash
pip install colorama
```

---

## 📝 Notes

This project follows the traditional **Memento Mori Calendar** layout:

- Each row represents one completed year of life.
- Each row contains **52 weeks**.
- The current week is calculated from your **most recent birthday**, matching the structure of the printed calendar.
- There is a picture of this calender available to print:
![link](https://github.com/rominva/memento-mori-calendar/blob/main/assets/Memento_Mori_Calendar.png)
or you can visit this site for more patterns 
https://lovelyplanner.com/printable-memento-mori-calendars/

---

## 📄 License

This project is licensed under the MIT License.
