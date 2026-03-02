import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('metrics.csv')

print("Colunas disponíveis:", df.columns.tolist())
print("\nPrimeiras 5 linhas:")
print(df.head())

columns = df.columns.tolist()

epoch_col = None
train_acc_col = None
val_acc_col = None
train_loss_col = None
val_loss_col = None

for col in columns:
    col_lower = col.lower().strip()
    if 'epoch' in col_lower or col_lower == 'epoch' or col_lower == 'epochs':
        epoch_col = col
        break


for col in columns:
    col_lower = col.lower().strip()
    if 'train' in col_lower and 'acc' in col_lower:
        train_acc_col = col
    if 'val' in col_lower and 'acc' in col_lower:
        val_acc_col = col

for col in columns:
    col_lower = col.lower().strip()
    if 'train' in col_lower and 'loss' in col_lower:
        train_loss_col = col
    if 'val' in col_lower and 'loss' in col_lower:
        val_loss_col = col

print(f"\nColunas detectadas:")
print(f"  Época: {epoch_col}")
print(f"  Train Accuracy: {train_acc_col}")
print(f"  Valid Accuracy: {val_acc_col}")
print(f"  Train Loss: {train_loss_col}")
print(f"  Valid Loss: {val_loss_col}")

if not all([train_acc_col, val_acc_col, train_loss_col, val_loss_col]):
    print("\nERRO: Não foi possível identificar todas as colunas necessárias.")
    print("O arquivo deve conter colunas com nomes como:")
    print("  - epoch (ou índice será usado)")
    print("  - train_acc e val_acc (ou variações com 'train', 'val', 'accuracy')")
    print("  - train_loss e val_loss (ou variações com 'train', 'val', 'loss')")
    exit(1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Gráfico 1: Model Accuracy
ax1.plot(df[epoch_col], df[train_acc_col],
         label='train', color='#1f77b4', linewidth=2)
ax1.plot(df[epoch_col], df[val_acc_col],
         label='valid', color='#ff7f0e', linewidth=2)
ax1.set_xlabel('epoch')
ax1.set_ylabel('accuracy')
ax1.set_title('model accuracy')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico 2: Model Loss
ax2.plot(df[epoch_col], df[train_loss_col],
         label='train', color='#1f77b4', linewidth=2)
ax2.plot(df[epoch_col], df[val_loss_col],
         label='valid', color='#ff7f0e', linewidth=2)
ax2.set_xlabel('epoch')
ax2.set_ylabel('loss')
ax2.set_title('model loss')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('training_curves.png', dpi=150, bbox_inches='tight')
print("\n Gráfico salvo como 'training_curves.png'")

plt.show()
