from numpy import sqrt
from numpy.random import rand, randn
import matplotlib.pyplot as plt

# https://scipy.github.io/old-wiki/pages/Cookbook/CommTheory.html
# http://www.eletrica.ufpr.br/evelio/TE111/Eb_N0.pdf

N = 5000000
EbNodB_range = range(0, 11)
itr = len(EbNodB_range)
ber = [None] * itr

for n in range(0, itr):
    EbNodB = EbNodB_range[n]
    EbNo = 10.0 ** (EbNodB / 10.0)
    x = 2 * (rand(N) >= 0.5) - 1
    noise_std = 1 / sqrt(2 * EbNo)
    y = x + noise_std * randn(N)
    y_d = 2 * (y >= 0) - 1
    errors = (x != y_d).sum()
    ber[n] = 1.0 * errors / N

    print("EbNodB:", EbNodB)
    print("Error bits:", errors)
    print("Error probability:", ber[n])

plt.plot(EbNodB_range, ber, 'bo', EbNodB_range, ber, 'k')
plt.axis([0, 10, 1e-6, 0.1])
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('EbNo(dB)')
plt.ylabel('BER')
plt.grid(True)
plt.title('BPSK Modulation')
plt.show()

# 0.0786638