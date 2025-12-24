import time
from collections import defaultdict, deque
from app.errors import APIError

_requests = defaultdict(deque)

def check_rate_limit(session_id: str):
    max_requests = 5
    window_seconds = 30

    now = time.time()
    window_start = now - window_seconds
    q = _requests[session_id]

    while q and q[0] < window_start:
        q.popleft()

    if len(q) >= max_requests:
        raise APIError(
            code="rate_limited",
            message="Too many messages. Please slow down.",
            status=429,
            details={
                "limit": max_requests,
                "window_seconds": window_seconds,
            },
        )

    q.append(now)
