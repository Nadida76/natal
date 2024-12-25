import matplotlib.pyplot as plt
import numpy as np


def desenhar_arvore(ax, niveis):
    # Desenha a parte da árvore
    for i in range(niveis):
        largura = 2 * (niveis - i)
        altura = 1

        # Cria um triângulo para cada nível da árvore
        x = [-largura / 2, 0, largura / 2]
        y = [i, i + altura, i]

        # Define uma cor aleatória para cada nível
        cor = np.random.rand(3, )
        ax.fill(x, y, color=cor)

        # Adiciona enfeites nas pontas com formas e cores aleatórias
        enfeite_x = [-largura / 2, largura / 2]
        enfeite_y = [i + altura, i + altura]
        for x in enfeite_x:
            forma = np.random.choice(['o', 's', 'D'])  # Círculo, quadrado, losango
            cor_enfeite = np.random.rand(3, )
            ax.plot(x, enfeite_y[0], forma, color=cor_enfeite, markersize=10)

    # Desenha o tronco da árvore
    tronco_x = [-0.2, 0.2, 0.2, -0.2]
    tronco_y = [0, 0, -0.5, -0.5]
    ax.fill(tronco_x, tronco_y, color='saddlebrown')


def adicionar_estrela(ax):
    # Adiciona uma estrela no topo da árvore
    estrela_x = [0, -0.1, 0.1]
    estrela_y = [niveis, niveis - 0.5, niveis - 0.5]
    ax.fill(estrela_x, estrela_y, color='gold')


def mensagem_feliz_natal(ax):
    # Adiciona a mensagem "Feliz Natal!" na parte inferior
    ax.text(0, -2.5, 'Feliz Natal!', fontsize=20, ha='center', color='red', fontweight='bold')


def adicionar_presentes(ax):
    # Adiciona várias caixas de presente embaixo da árvore
    for _ in range(10):  # Adiciona 10 presentes
        x = np.random.uniform(-0.8, 0.8)
        y = np.random.uniform(-1, -1)  # Ajusta a posição para ficar acima da mensagem
        cor_presente = np.random.rand(3, )
        ax.add_patch(plt.Rectangle((x - 0.1, y), 0.3, 0.2, color=cor_presente, ec='black'))
        ax.add_patch(plt.Rectangle((x - 0.1, y), 0.2, 0.1, color='red', ec='black'))


def adicionar_flocos_de_neve(ax, num_flocos):
    # Adiciona flocos de neve aleatórios
    for _ in range(num_flocos):
        x = np.random.uniform(-niveis, niveis)
        y = np.random.uniform(0, niveis)
        ax.plot(x, y, 'o', color='white', markersize=5)


def criar_arvore_natal(niveis):
    fig, ax = plt.subplots()
    ax.set_xlim(-niveis, niveis)
    ax.set_ylim(-4, niveis)
    ax.axis('off')  # Desliga os eixos

    # Adiciona um fundo colorido
    ax.set_facecolor('lightblue')

    desenhar_arvore(ax, niveis)
    adicionar_estrela(ax)
    mensagem_feliz_natal(ax)
    adicionar_presentes(ax)
    adicionar_flocos_de_neve(ax, 50)  # Adiciona 50 flocos de neve

    plt.title('Árvore de Natal', fontsize=24, color='green', fontweight='bold')
    plt.show()


if __name__ == "__main__":
    # Número de níveis da árvore
    niveis = 5
    criar_arvore_natal(niveis)