# Red Wine Quality Prediction — Regression

A machine learning project that predicts the quality score of red wine based on physicochemical properties using a Random Forest model, with a Streamlit web application for real-time quality estimation.

---

## English

### About

This project trains a Random Forest regression model on the UCI Red Wine Quality dataset to predict wine quality scores (0–10) from chemical measurements such as acidity, alcohol content, sulphates, and residual sugar. The trained model is served through a Streamlit web app where users can input wine properties and receive an estimated quality score.

### Features

- Regression: predicts wine quality score (0–10)
- 11 physicochemical input features: fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free/total SO₂, density, pH, sulphates, alcohol
- Random Forest regressor (`model.pkl`)
- Streamlit web app for real-time quality estimation

### Dataset

**Source:** [UCI Machine Learning Repository — Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality) / [Kaggle](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

| File | Size | Status |
|---|---|---|
| `winequality-red.csv` | 100 KB | ✅ Included |

1,599 red wine samples with 11 features and a `quality` score from 0 to 10.

### Model Architecture / Tech Stack

```
Physicochemical Properties (11 features)
→ Feature Scaling
→ Random Forest Regressor
→ Quality Score (0–10)
```

**Tech Stack:** Python · scikit-learn · pandas · NumPy · joblib · Streamlit

### How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Enter wine physicochemical values in the Streamlit app to get a predicted quality score.

### Requirements

```
pandas
numpy
scikit-learn
streamlit
joblib
```

---

## Türkçe

### Hakkında

Bu proje, asitlik, alkol içeriği, sülfatlar ve artık şeker gibi kimyasal ölçümlerden şarap kalite puanlarını (0–10) tahmin etmek için UCI Kırmızı Şarap Kalitesi veri seti üzerinde Rastgele Orman regresyon modeli eğitir. Eğitilen model, bir Streamlit web uygulamasıyla sunulur; kullanıcılar şarap özelliklerini girerek tahmini kalite puanı alabilir.

### Özellikler

- Regresyon: şarap kalite puanı tahmini (0–10)
- 11 fizikokimyasal giriş özelliği: sabit asitlik, uçucu asitlik, sitrik asit, artık şeker, klorürler, serbest/toplam SO₂, yoğunluk, pH, sülfatlar, alkol
- Rastgele Orman regresörü (`model.pkl`)
- Gerçek zamanlı kalite tahmini için Streamlit web uygulaması

### Veri Seti

**Kaynak:** [UCI Makine Öğrenimi Deposu — Şarap Kalitesi](https://archive.ics.uci.edu/dataset/186/wine+quality) / [Kaggle](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

| Dosya | Boyut | Durum |
|---|---|---|
| `winequality-red.csv` | 100 KB | ✅ Dahil |

11 özellik ve 0 ile 10 arasında `quality` puanına sahip 1.599 kırmızı şarap örneği.

### Model Mimarisi / Teknoloji Yığını

```
Fizikokimyasal Özellikler (11 özellik)
→ Özellik Ölçeklendirme
→ Rastgele Orman Regresörü
→ Kalite Puanı (0–10)
```

**Teknoloji Yığını:** Python · scikit-learn · pandas · NumPy · joblib · Streamlit

### Nasıl Çalıştırılır

```bash
pip install -r requirements.txt
streamlit run app.py
```

Streamlit uygulamasına şarabın fizikokimyasal değerlerini girerek tahmini kalite puanını alın.

### Gereksinimler

```
pandas
numpy
scikit-learn
streamlit
joblib
```
