from torch import nn

class ImageClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(1, 4, (3,3)),
            nn.ReLU(),
            nn.Conv2d(4, 8, (3,3)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(8*(28-4)*(28-4), 10)
        )
    def forward(self,x):
        return self.model(x)