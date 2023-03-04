"""Модуль графиков.

Импорты:
    import pandas as pd - для работы с данными
    from matplotlib import ... - для работы с графиками

Функции:
    _init_subplots - инициализировать plots
    _setup_axis - настроить ось
    build_qualitative_charts - построить графики качественной переменной
    build_quantitative_charts - построить графики количественной переменной

"""
import pandas as pd
from matplotlib import pyplot as plt


def _init_subplots(num: int, title: str) -> list[plt.Axes]:
    """Инициализировать plots.

    Аргументы:
        num: int - количество графиков
        title: str - заголовок графиков

    Возвращает список созданных осей

    """
    fig, axes = plt.subplots(1, num)
    fig.set_figwidth(num * 9)
    plt.suptitle(title)
    return axes


def _setup_axis(axis: plt.Axes, title: str, ylabel: str):
    """Настроить ось.

    Аргументы:
        axis: plt.Axes - ось
        title: str - заголовок графика
        ylabel: str - подпись y

    """
    axis.set_title(title)
    axis.set_xlabel("Значения", labelpad=15)
    axis.set_ylabel(ylabel, labelpad=15)


def build_qualitative_charts(data: pd.Series, title: str):
    """Построить графики качественной переменной.

    Аргументы:
        data: pd.Series - данные переменной
        title: str - заголовок графиков

    """
    axes = _init_subplots(2, title)
    value_counts = data.value_counts()

    _setup_axis(axes[0], "Столбчатая диагармма", "Количество")
    axes[0].tick_params("x", labelrotation=90)
    axes[0].bar(value_counts.index, value_counts)

    axes[1].set_title("Круговая диаграмма")
    axes[1].pie(value_counts, autopct="%1.2f%%", pctdistance=1.2)
    axes[1].legend(value_counts.index, title="Значения",
                   bbox_to_anchor=(1.08, 1))

    plt.show()


def build_quantitative_charts(data: pd.Series, title: str):
    """Построить графики количественной переменной.

    Аргументы:
        data: pd.Series - данные переменной
        title: str - заголовок графиков

    """
    axes = _init_subplots(3, title)
    seq = data.dropna()

    _setup_axis(axes[0], "Гистограмма", "Частота")
    axes[0].hist(seq)

    seq.plot.kde(0.1, ax=axes[1])
    _setup_axis(axes[1], "График плотности", "Плотность")

    _setup_axis(axes[2], "Диаграмма размаха", title)
    axes[2].tick_params("y", labelleft=False)
    axes[2].boxplot(seq, vert=False)

    plt.show()
