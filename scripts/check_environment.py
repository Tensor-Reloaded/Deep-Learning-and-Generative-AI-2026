"""Small offline CPU check for this semester's PyTorch environment."""
import sys
import torch
import torchvision
from torch import nn
from torch.utils.data import TensorDataset, DataLoader

torch.manual_seed(42)
torch.set_num_threads(1)
inputs = torch.tensor([[-2., -1.], [-1., -2.], [1., 2.], [2., 1.]])
targets = torch.tensor([0, 0, 1, 1], dtype=torch.long)
model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2))
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=.1)

initial_loss = criterion(model(inputs), targets).item()
original = [parameter.detach().clone() for parameter in model.parameters()]
for _ in range(60):
    optimizer.zero_grad(set_to_none=True)
    logits = model(inputs)
    assert logits.shape == (4, 2)
    loss = criterion(logits, targets)
    loss.backward()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())
    optimizer.step()

model.eval()
with torch.no_grad():
    final_loss = criterion(model(inputs), targets).item()
    assert final_loss < initial_loss * .25
    assert torch.equal(model(inputs).argmax(dim=1), targets)
assert any(not torch.equal(old, new) for old, new in zip(original, model.parameters()))
loader = DataLoader(TensorDataset(inputs, targets), batch_size=2, shuffle=False, num_workers=0)
assert sum(len(batch_targets) for _, batch_targets in loader) == len(inputs)
print(f"Python {sys.version.split()[0]}; torch {torch.__version__}; torchvision {torchvision.__version__}")
print(f"CPU smoke check passed; synthetic training loss {initial_loss:.4f} -> {final_loss:.4f}")
print(f"Available: CUDA={torch.cuda.is_available()}, MPS={torch.backends.mps.is_available()}")
