import pandas as pd
import os

print("Arquivos CSV nesta pasta:")
for arquivo in os.listdir('.'):
    if arquivo.endswith('.csv'):
        print(f"  - {arquivo}")
print()

data = pd.read_csv('classification_results_trial_0001.csv')

print("1. Quantas imagens são benign e malign em real_class?")
print(data['real_class'].value_counts())
print()

print("2. Imagens onde o modelo errou:")
erros = data[data['real_class'] != data['predicted_class']]
print(erros[['image_path', 'real_class', 'predicted_class']])
print()

print("3. Confiança do modelo nos erros:")
erros['confianca'] = erros.apply(
    lambda row: row['prob_malign'] if row['predicted_class'] == 'malign' else row['prob_benign'],
    axis=1
)
print(erros[['image_path', 'real_class', 'predicted_class', 'confianca']])
print()

print("4. Matriz de Confusão:")
TP = len(data[(data['real_class'] == 'malign') &
         (data['predicted_class'] == 'malign')])
TN = len(data[(data['real_class'] == 'benign') &
         (data['predicted_class'] == 'benign')])
FP = len(data[(data['real_class'] == 'benign') &
         (data['predicted_class'] == 'malign')])
FN = len(data[(data['real_class'] == 'malign') &
         (data['predicted_class'] == 'benign')])
print(f"TP: {TP}")
print(f"TN: {TN}")
print(f"FP: {FP}")
print(f"FN: {FN}")
print()

print("5. Métricas:")
acuracia = (TP + TN) / (TP + TN + FP + FN)
precisao = TP / (TP + FP)
recall = TP / (TP + FN)
especificidade = TN / (TN + FP)
print(f"Acurácia: {acuracia:.4f}")
print(f"Precisão: {precisao:.4f}")
print(f"Recall: {recall:.4f}")
print(f"Especificidade: {especificidade:.4f}")
print()

print("6. Top 5 imagens benign com menor prob_benign:")
benign = data[data['real_class'] == 'benign']
print(benign.nsmallest(5, 'prob_benign')[
      ['image_path', 'prob_benign', 'prob_malign']])
print()

print("7. Top 5 imagens malign com maior prob_benign:")
malign = data[data['real_class'] == 'malign']
print(malign.nlargest(5, 'prob_benign')[
      ['image_path', 'prob_benign', 'prob_malign']])
