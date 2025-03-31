from typing import Tuple, List, Union


def get_norm(point0: Tuple[int, int], point1: Tuple[int, int]) -> int:
    return (point0[0] - point1[0]) ** 2 + (point0[1] - point1[1]) ** 2


def get_mst_lens(points: List[Tuple[int, int]]) -> List[int]:
    """
    :param points: Координаты точек
    :return: Нормы ребер MST
    """
    mst_edges_lens: List[int] = []

    min_norms_to_current_mst: List[Union[float('inf'), None, int]] = [float('inf')] * len(points)
    min_norms_to_current_mst[0] = None

    last_vertex: int = 0
    while True:
        min_edge_norma = float('inf')
        min_edge_vertex = None
        for i in range(len(min_norms_to_current_mst)):
            if min_norms_to_current_mst[i] is None: continue # если вершина уже в MST

            # обновляем минимальные расстояния до MST
            min_norms_to_current_mst[i] = min(min_norms_to_current_mst[i], get_norm(points[i], points[last_vertex]))

            # обновляем минимум расстояний до MST
            if min_edge_norma > min_norms_to_current_mst[i]:
                min_edge_norma = min_norms_to_current_mst[i]
                min_edge_vertex = i

        if min_edge_vertex is None: break
        mst_edges_lens.append(min_edge_norma)
        last_vertex = min_edge_vertex
        min_norms_to_current_mst[last_vertex] = None

    return mst_edges_lens
