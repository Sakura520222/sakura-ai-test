CIALLO_GREETING = "Ciallo～(∠・ω< )⌒☆"


def main() -> None:
    print("Hello, Sakura-AI!")
    try:
        print(CIALLO_GREETING)
    except UnicodeEncodeError:
        # 部分控制台编码（如 Windows 的 GBK/cp936）无法表示颜文字，降级为 ASCII 输出
        print("Ciallo~")


if __name__ == "__main__":
    main()
