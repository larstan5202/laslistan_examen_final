# Läslistan – Examinationsprojekt

Detta projekt är en testsvit för webbsidan **Läslistan**, enligt kursens examinationsuppgift.  
Projektet innehåller backend‑kod, enhetstester, integrationstester, user stories, feature‑filer och step‑definitioner.

---

## 📘 Backend – Vad som testas

Backend består av två klasser:

### **FavoriteBooks**
- `add(book)`
- `remove(book)`

### **BookStore**
- `addBook(author, title)`
- `toggleFavorite(book_id)`

### Tester som ingår:
✔ Enhetstester för alla metoder  
✔ Integrationstest som verifierar att BookStore och FavoriteBooks fungerar tillsammans  

Alla tester körs med **pytest**.

---

## 🌐 Frontend – Vad som testas

Frontend‑delen testas med **Behave + Playwright**.

### Funktionalitet som testas:
✔ Visa bokkatalog  
✔ Markera bok som favorit  
✔ Avmarkera favoritbok  
✔ Lägga till ny bok  

### Artefakter:
- `STORIES.md` – user stories
- `.feature`‑filer – BDD‑scenarier
- `steps/` – step‑definitioner i Python

---

## 🚀 Så här kör du projektet

### 1. Installera beroenden
```bash
pip install -r requirements.txt
