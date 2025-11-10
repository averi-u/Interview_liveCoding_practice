"""
Q2: Minimum Cost to Connect Servers

There are n servers with distinct, sorted capacities.
Two connection rules:

1. You may connect servers i and j for cost |capacity[i] - capacity[j]|.
   This can be simulated by walking along adjacent servers in sorted order,
   since sum of adjacent gaps == full direct difference.

2. Each server x has exactly one closest neighbor (either x-1 or x+1).
   You may connect x and its closest neighbor for fixed cost 1.
   This cheap edge is undirected.

Queries:
    For each (fromServer, toServer), find the minimum cost to connect them.

Graph construction:
    - Add weighted edges between adjacent capacities.
    - Add a cost-1 edge between each node and its closest neighbor.

Solve each unique source with Dijkstra and reuse results for all queries
originating from that source.

Overall complexity: O((n + q) log n).
"""
def getMinCost(capacity, fromServer, toServer):
    import heapq

    n = len(capacity)
    # Sort servers by capacity; keep index maps
    order = sorted(range(n), key=lambda i: capacity[i])
    pos = [0]*n
    for idx, orig in enumerate(order):
        pos[orig] = idx

    # Build sparse graph:
    # 1) path edges between adjacent capacities (simulate any-server costs)
    # 2) cheap edges (cost 1) to each node's unique closest neighbor
    adj = [[] for _ in range(n)]

    # (1) adjacent weighted edges
    for i in range(n-1):
        a = order[i]
        b = order[i+1]
        w = abs(capacity[a] - capacity[b])  # equals capacity[b]-capacity[a]
        adj[a].append((b, w))
        adj[b].append((a, w))

    # (2) closest-neighbor edges (cost 1)
    for i in range(n):
        p = pos[i]
        # candidates: left/right neighbors in sorted order if they exist
        best_j = None
        if p > 0:
            left = order[p-1]
            best_j = left
        if p+1 < n:
            right = order[p+1]
            if best_j is None:
                best_j = right
            else:
                dl = abs(capacity[i] - capacity[best_j])
                dr = abs(capacity[i] - capacity[right])
                if dr < dl:
                    best_j = right
        # add an UNDIRECTED cheap edge with weight 1
        if best_j is not None:
            adj[i].append((best_j, 1))
            adj[best_j].append((i, 1))

    # Group queries by source so we run Dijkstra at most once per source
    q = len(fromServer)
    by_src = {}
    for qid, (s, t) in enumerate(zip(fromServer, toServer)):
        by_src.setdefault(s, []).append((qid, t))

    res = [0]*q

    def dijkstra(src):
        dist = [float('inf')]*n
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist

    for s, items in by_src.items():
        dist = dijkstra(s)
        for qid, t in items:
            res[qid] = int(dist[t])

    return res


"""
Q3: Maximum Team Size (Interval Overlap Star Condition)

You are given n employees with working intervals [startTime[i], endTime[i]].
Two employees can interact if their intervals overlap (inclusive).

A team is valid if there exists at least one employee who overlaps with
every other member. This "hub" employee doesn’t need everyone to overlap
simultaneously; they just need pairwise overlap.

Goal:
    Compute the size of the largest possible valid team.

Approach:
    For each interval i, count how many intervals overlap with i.
    Use sorted start times and sorted end times with binary search to
    compute inclusive-overlap counts in O(n log n).
"""