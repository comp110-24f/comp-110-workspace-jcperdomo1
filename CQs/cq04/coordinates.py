def get_coords(xs: str, ys: str) -> None:
    idx = 0
    while idx < len(xs):
        xcoord = xs[idx]
        idx2 = 0
        while idx2 < len(ys):
            ycoord = ys[idx2]
            print(f"({xcoord},{ycoord})")
            idx2 += 1
        idx += 1


if __name__ == "main":
    get_coords("hi", "bye")
