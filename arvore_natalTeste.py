import matplotlib.pyplot as plt
import numpy as np


def desenhar_arvore(ax, niveis, cores_enfeites):
    """Desenha a árvore de Natal e os enfeites."""
    for i in range(niveis):
        largura = 2 * (niveis - i)
        altura = 1

        # Cria um triângulo para cada nível da árvore
        x = [-largura / 2, 0, largura / 2]
        y = [i, i + altura, i]

        ax.fill(x, y, color='green')

        # Adiciona enfeites nas pontas com cores fornecidas
        enfeite_x = [-largura / 2, largura / 2]
        for x in enfeite_x:
            ax.plot(x, i + altura, 'o', color=cores_enfeites[i % len(cores_enfeites)], markersize=10)

    # Desenha o tronco da árvore
    tronco_x = [-0.2, 0.2, 0.2, -0.2]
    tronco_y = [0, 0, -0.5, -0.5]
    ax.fill(tronco_x, tronco_y, color='saddlebrown')


def adicionar_estrela(ax):
    """Adiciona uma estrela no topo da árvore."""
    estrela_x = [0, -0.1, 0.1]
    estrela_y = [niveis, niveis - 0.5, niveis - 0.5]
    ax.fill(estrela_x, estrela_y, color='gold')


def mensagem_feliz_natal(ax):
    """Adiciona a mensagem 'Feliz Natal!' na parte inferior."""
    ax.text(0, -2.5, 'Feliz Natal!', fontsize=20, ha='center', color='red', fontweight='bold')


def adicionar_presentes(ax):
    """Adiciona várias caixas de presente embaixo da árvore."""
    for _ in range(10):  # Adiciona 10 presentes
        x = np.random.uniform(-0.8, 0.8)
        y = np.random.uniform(-2.5, -1)  # Ajusta a posição para ficar acima da mensagem
        cor_presente = np.random.rand(3, )
        ax.add_patch(plt.Rectangle((x - 0.1, y), 0.2, 0.2, color=cor_presente, ec='black'))
        ax.add_patch(plt.Rectangle((x - 0.1, y), 0.2, 0.1, color='red', ec='black'))


def adicionar_flocos_de_neve(ax, num_flocos):
    """Adiciona flocos de neve aleatórios."""
    for _ in range(num_flocos):
        x = np.random.uniform(-niveis, niveis)
        y = np.random.uniform(0, niveis)
        ax.plot(x, y, 'o', color='white', markersize=5)


def criar_arvore_natal(niveis):
    """Cria a árvore de Natal e anima o efeito de luzes."""
    fig, ax = plt.subplots()
    ax.set_xlim(-niveis, niveis)
    ax.set_ylim(-4, niveis)
    ax.axis('off')  # Desliga os eixos

    # Adiciona um fundo colorido
    ax.set_facecolor('lightblue')

    # Cores dos enfeites
    cores_enfeites = ['red', 'yellow', 'blue', 'purple', 'orange']

    while True:
        # Desenha a árvore
        ax.clear()
        ax.set_xlim(-niveis, niveis)
        ax.set_ylim(-4, niveis)
        ax.axis('off')

        # Desenha a árvore com enfeites
        desenhar_arvore(ax, niveis, cores_enfeites)
        adicionar_estrela(ax)
        mensagem_feliz_natal(ax)
        adicionar_presentes(ax)
        adicionar_flocos_de_neve(ax, 50)  # Adiciona 50 flocos de neve

        # Atualiza a tela
        plt.draw()
        plt.pause(0.5)  # Pausa para criar o efeito de piscar

        # Altera as cores dos enfeites
        cores_enfeites = np.random.choice(cores_enfeites, size=len(cores_enfeites), replace=False)

        # Atualiza a tela novamente
        ax.clear()
        ax.set_xlim(-niveis, niveis)
        ax.set_ylim(-4, niveis)
        ax.axis('off')

        # Desenha a árvore com as novas cores dos enfeites
        desenhar_arvore(ax, niveis, cores_enfeites)
        adicionar_estrela(ax)
        mensagem_feliz_natal(ax)
        adicionar_presentes(ax)
        adicionar_flocos_de_neve(ax, 50)  # Adiciona 50 flocos de neve

        # Atualiza a tela
        plt.title('Árvore de Natal', fontsize=24, color='green', fontweight='bold')
        plt.draw()
        plt.pause(0.5)  # Pausa para criar o efeito de piscar

if __name__ == "__main__":
    # Número de níveis da árvore
    niveis = 5
    criar_arvore_natal(niveis)