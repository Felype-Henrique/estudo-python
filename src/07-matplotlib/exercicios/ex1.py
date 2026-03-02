import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


def load_data():
    csv_path = 'classification_results_trial_0001.csv'

    if os.path.exists(csv_path):
        print(f"Arquivo encontrado: {csv_path}")
        df = pd.read_csv(csv_path)

        data = {
            'image_path': [f'image_{i:03d}.jpg' for i in range(1, 101)],
            'real_class': np.random.choice(['benign', 'malign'], 100, p=[0.6, 0.4]),
            'predicted_class': [],
            'prob_benign': [],
            'prob_malign': []
        }

        for real in data['real_class']:
            if real == 'benign':
                prob_benign = np.random.beta(5, 2)
            else:
                prob_benign = np.random.beta(2, 5)

            prob_malign = 1 - prob_benign
            predicted = 'benign' if prob_benign > 0.5 else 'malign'

            data['prob_benign'].append(prob_benign)
            data['prob_malign'].append(prob_malign)
            data['predicted_class'].append(predicted)

        df = pd.DataFrame(data)

    return df


def analyze_data(df):
    print("=" * 60)
    print("ANÁLISE DOS DADOS DE CLASSIFICAÇÃO")
    print("=" * 60)
    print(f"\nTotal de amostras: {len(df)}")
    print(f"\nDistribuição das classes reais:")
    print(df['real_class'].value_counts())
    print(f"\nDistribuição das classes preditas:")
    print(df['predicted_class'].value_counts())

    df['correct'] = df['real_class'] == df['predicted_class']
    accuracy = df['correct'].mean()
    print(f"\n Acurácia geral: {accuracy:.2%}")

    print("\n" + "=" * 60)
    print("MATRIZ DE CONFUSÃO")
    print("=" * 60)
    tp = len(df[(df['real_class'] == 'malign') &
             (df['predicted_class'] == 'malign')])
    tn = len(df[(df['real_class'] == 'benign') &
             (df['predicted_class'] == 'benign')])
    fp = len(df[(df['real_class'] == 'benign') &
             (df['predicted_class'] == 'malign')])
    fn = len(df[(df['real_class'] == 'malign') &
             (df['predicted_class'] == 'benign')])

    print(
        f"\nVerdadeiro Positivo (TP): {tp} - Corretamente identificou maligno")
    print(f"Verdadeiro Negativo (TN): {tn} - Corretamente identificou benigno")
    print(f"Falso Positivo (FP): {fp} - Erro: disse maligno, era benigno")
    print(f"Falso Negativo (FN): {fn} - Erro: disse benigno, era maligno")

    return df, tp, tn, fp, fn


def create_visualizations(df, tp, tn, fp, fn):
    fig = plt.figure(figsize=(16, 12))

    ax1 = plt.subplot(3, 3, 1)
    real_counts = df['real_class'].value_counts()
    colors_real = ['#2ecc71' if x ==
                   'benign' else '#e74c3c' for x in real_counts.index]
    ax1.bar(real_counts.index, real_counts.values,
            color=colors_real, alpha=0.7, edgecolor='black')
    ax1.set_title('Distribuição das Classes Reais',
                  fontweight='bold', fontsize=12)
    ax1.set_xlabel('Classe Real')
    ax1.set_ylabel('Contagem')
    ax1.grid(axis='y', alpha=0.3)
    for i, v in enumerate(real_counts.values):
        ax1.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')

    ax2 = plt.subplot(3, 3, 2)
    pred_counts = df['predicted_class'].value_counts()
    colors_pred = ['#2ecc71' if x ==
                   'benign' else '#e74c3c' for x in pred_counts.index]
    ax2.bar(pred_counts.index, pred_counts.values,
            color=colors_pred, alpha=0.7, edgecolor='black')
    ax2.set_title('Distribuição das Predições', fontweight='bold', fontsize=12)
    ax2.set_xlabel('Classe Predita')
    ax2.set_ylabel('Contagem')
    ax2.grid(axis='y', alpha=0.3)
    for i, v in enumerate(pred_counts.values):
        ax2.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')

    ax3 = plt.subplot(3, 3, 3)
    ax3.hist(df['prob_benign'], bins=30, color='#2ecc71',
             alpha=0.7, edgecolor='black')
    ax3.axvline(0.5, color='red', linestyle='--',
                linewidth=2, label='Threshold (0.5)')
    ax3.set_title('Distribuição de Probabilidade Benigno',
                  fontweight='bold', fontsize=12)
    ax3.set_xlabel('Probabilidade Benigno')
    ax3.set_ylabel('Frequência')
    ax3.legend()
    ax3.grid(alpha=0.3)

    ax4 = plt.subplot(3, 3, 4)
    ax4.hist(df['prob_malign'], bins=30, color='#e74c3c',
             alpha=0.7, edgecolor='black')
    ax4.axvline(0.5, color='red', linestyle='--',
                linewidth=2, label='Threshold (0.5)')
    ax4.set_title('Distribuição de Probabilidade Maligno',
                  fontweight='bold', fontsize=12)
    ax4.set_xlabel('Probabilidade Maligno')
    ax4.set_ylabel('Frequência')
    ax4.legend()
    ax4.grid(alpha=0.3)

    ax5 = plt.subplot(3, 3, 5)
    correct_mask = df['correct']
    ax5.scatter(df[correct_mask]['prob_benign'],
                df[correct_mask]['prob_malign'],
                c='#3498db', label='Acerto', alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
    ax5.scatter(df[~correct_mask]['prob_benign'],
                df[~correct_mask]['prob_malign'],
                c='#e67e22', label='Erro', alpha=0.8, s=80, marker='X', edgecolors='black', linewidth=0.5)
    ax5.plot([0, 1], [1, 0], 'r--', linewidth=2, label='Limite de decisão')
    ax5.set_title('Probabilidades: Benigno vs Maligno',
                  fontweight='bold', fontsize=12)
    ax5.set_xlabel('Probabilidade Benigno')
    ax5.set_ylabel('Probabilidade Maligno')
    ax5.legend()
    ax5.grid(alpha=0.3)
    ax5.set_xlim(-0.05, 1.05)
    ax5.set_ylim(-0.05, 1.05)

    ax6 = plt.subplot(3, 3, 6)
    error_types = ['Falso Positivo\n(FP)', 'Falso Negativo\n(FN)']
    error_counts = [fp, fn]
    colors_errors = ['#f39c12', '#c0392b']
    bars = ax6.bar(error_types, error_counts, color=colors_errors,
                   alpha=0.7, edgecolor='black', linewidth=2)
    ax6.set_title('Comparação de Tipos de Erro',
                  fontweight='bold', fontsize=12)
    ax6.set_ylabel('Contagem')
    ax6.grid(axis='y', alpha=0.3)

    for i, (bar, count) in enumerate(zip(bars, error_counts)):
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height,
                 f'{count}\n({count/(fp+fn)*100:.1f}%)' if (fp +
                                                            fn) > 0 else '0',
                 ha='center', va='bottom', fontweight='bold', fontsize=11)

    if fp > fn:
        most_common = f"FP é mais comum ({fp} vs {fn})"
    elif fn > fp:
        most_common = f"FN é mais comum ({fn} vs {fp})"
    else:
        most_common = f"FP e FN são iguais ({fp})"

    ax6.text(0.5, -0.25, most_common, transform=ax6.transAxes,
             ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    ax7 = plt.subplot(3, 3, 7)
    confusion_matrix = np.array([[tn, fp], [fn, tp]])
    im = ax7.imshow(confusion_matrix, cmap='YlOrRd', alpha=0.7)

    ax7.set_xticks([0, 1])
    ax7.set_yticks([0, 1])
    ax7.set_xticklabels(['Predito: Benigno', 'Predito: Maligno'])
    ax7.set_yticklabels(['Real: Benigno', 'Real: Maligno'])
    ax7.set_title('Matriz de Confusão', fontweight='bold', fontsize=12)

    for i in range(2):
        for j in range(2):
            text = ax7.text(j, i, f'{confusion_matrix[i, j]}\n',
                            ha="center", va="center", color="black", fontweight='bold', fontsize=14)
            if i == 0 and j == 0:
                label = "TN"
            elif i == 0 and j == 1:
                label = "FP"
            elif i == 1 and j == 0:
                label = "FN"
            else:
                label = "TP"
            ax7.text(j, i + 0.15, f'({label})', ha="center", va="center",
                     color="darkred", fontsize=9, style='italic')

    ax8 = plt.subplot(3, 3, 8)
    ax8.axis('off')

    accuracy = (tp + tn) / (tp + tn + fp +
                            fn) if (tp + tn + fp + fn) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision +
                                           recall) if (precision + recall) > 0 else 0

    metrics_text = f"""
    MÉTRICAS DE DESEMPENHO
    {'=' * 35}
    
    Acurácia: {accuracy:.2%}
    
    Precisão: {precision:.2%}
    (Dos que predisse maligno, 
     quantos eram realmente malignos)
    
    Recall/Sensibilidade: {recall:.2%}
    (Dos malignos reais, 
     quantos foram detectados)
    
    Especificidade: {specificity:.2%}
    (Dos benignos reais,
     quantos foram corretamente identificados)
    
    F1-Score: {f1_score:.2%}
    (Média harmônica de precisão e recall)
    """

    ax8.text(0.1, 0.5, metrics_text, fontsize=10, family='monospace',
             verticalalignment='center', bbox=dict(boxstyle='round',
                                                   facecolor='lightblue', alpha=0.3))

    ax9 = plt.subplot(3, 3, 9)
    ax9.axis('off')

    medical_analysis = f"""
    CONTEXTO MÉDICO
    {'=' * 35}
    
    ERRO MAIS PREOCUPANTE:
    
    FALSO NEGATIVO (FN) = {fn}
    
    Por quê?
    • FN = dizer que é BENIGNO quando 
      é MALIGNO
    • Paciente com câncer não recebe 
      tratamento
    • Pode levar à progressão da doença
    • Consequências potencialmente FATAIS
    
    vs.
    
    Falso Positivo (FP) = {fp}
    • FP = dizer que é MALIGNO quando 
      é BENIGNO
    • Ansiedade e testes adicionais
    • Menos grave que FN
    
     Em oncologia, é preferível ter
      mais FPs do que FNs (cautela)
    """

    ax9.text(0.1, 0.5, medical_analysis, fontsize=9, family='monospace',
             verticalalignment='center', bbox=dict(boxstyle='round',
                                                   facecolor='#ffe6e6', alpha=0.5))

    plt.tight_layout()
    plt.savefig('classification_analysis.png', dpi=300, bbox_inches='tight')
    print("\n Gráficos salvos em: classification_analysis.png")

    return fig


def print_medical_context(fp, fn):
    print("\n" + "=" * 60)
    print("ANÁLISE DO CONTEXTO MÉDICO")
    print("=" * 60)

    print(f"\nERRO MAIS COMUM:")
    if fp > fn:
        print(f"   Falso Positivo (FP) = {fp} casos")
        print(f"   Falso Negativo (FN) = {fn} casos")
        print(f"   → FP é {fp - fn} caso(s) mais frequente")
    elif fn > fp:
        print(f"   Falso Negativo (FN) = {fn} casos")
        print(f"   Falso Positivo (FP) = {fp} casos")
        print(f"   → FN é {fn - fp} caso(s) mais frequente")
    else:
        print(f"   Falso Positivo (FP) = {fp} casos")
        print(f"   Falso Negativo (FN) = {fn} casos")
        print(f"   → FP e FN têm a mesma frequência")

    print(f"\nERRO MAIS PREOCUPANTE NO CONTEXTO MÉDICO:")
    print("   FALSO NEGATIVO (FN)")

    print("\nJUSTIFICATIVA:")
    print("\n   FALSO NEGATIVO (FN):")
    print("   • Definição: Classificar como BENIGNO um tumor que é MALIGNO")
    print("   • Impacto: Paciente com câncer NÃO recebe tratamento adequado")
    print("   • Consequências:")
    print("     - Progressão da doença sem intervenção")
    print("     - Metástase (espalhamento do câncer)")
    print("     - Redução significativa das chances de cura")
    print("     - Risco de morte")
    print("   • Gravidade:CRÍTICA")

    print("\n   FALSO POSITIVO (FP):")
    print("   • Definição: Classificar como MALIGNO um tumor que é BENIGNO")
    print("   • Impacto: Paciente saudável passa por procedimentos desnecessários")
    print("   • Consequências:")
    print("     - Ansiedade e estresse psicológico")
    print("     - Exames adicionais (biópsia, ressonância)")
    print("     - Custos financeiros")
    print("     - Possíveis procedimentos invasivos desnecessários")
    print("   • Gravidade: MODERADA (menos grave que FN)")

    print("\nPRINCÍPIO MÉDICO:")
    print("   Em diagnóstico de câncer, é preferível ter MAIS FALSOS POSITIVOS")
    print("   do que FALSOS NEGATIVOS. É melhor investigar mais casos (cautela)")
    print("   do que deixar passar um câncer verdadeiro.")

    print("\nMÉTRICAS RELEVANTES:")
    print("   • RECALL/SENSIBILIDADE: O quão bem o modelo detecta malignos")
    print("     (alta sensibilidade minimiza FN)")
    print("   • ESPECIFICIDADE: O quão bem o modelo detecta benignos")
    print("     (alta especificidade minimiza FP)")
    print("\n   Trade-off: Geralmente aumentar uma métrica reduz a outra.")
    print("      Em oncologia, prioriza-se RECALL (minimizar FN).")

    print("\n" + "=" * 60)


def main():
    print("\n" + "=" * 60)
    print("VISUALIZAÇÃO DE CLASSIFICAÇÃO MÉDICA - ex01.py")
    print("=" * 60 + "\n")

    df = load_data()
    df, tp, tn, fp, fn = analyze_data(df)
    create_visualizations(df, tp, tn, fp, fn)
    print_medical_context(fp, fn)

    print("\n" + "=" * 60)
    print(" Análise completa!")
    print("=" * 60 + "\n")

    plt.show()


if __name__ == "__main__":
    main()
