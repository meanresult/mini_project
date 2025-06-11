import IF_project as ifp
import datetime
#IF_project #폴더임
#funtion.py
#var.py






while True:
    orders = []

    while True:
        # 메뉴 선택
        order_num = ifp.funtion.select_menu()
        if order_num is None:
            continue
        selected_menu = ifp.var.menu_list[order_num]

        # 맛 선택
        selected_flavors = ifp.funtion.select_flavors(selected_menu)
        if selected_flavors is None or not selected_flavors:
            continue

        # 장바구니 담기
        if not ifp.funtion.cart(orders, selected_menu, selected_flavors):
            continue

        # 장바구니 담은 이후 선택지 루프
        while True:
            action = ifp.funtion.after_cart_menu()

            if action == '1':  # 추가 주문
                break  # 내부 루프 종료, 상위 루프에서 다시 주문

            elif action == '2':  # 주문 내역 보기
                print("\n 현재 주문 내역:")
                ifp.funtion.show_orders(orders)
                print()

            elif action == '3':  # 주문 취소
                ifp.funtion.canceled(orders)
                if not orders:
                    print("모든 주문이 취소되어 처음으로 돌아갑니다.\n")
                    break  # 내부 루프 종료
            elif action == '4':  # 결제 진행
                break  # 내부 루프 종료, 결제로 진행

        # 주문이 모두 취소된 경우 전체 루프 재시작
        if not orders:
            break

        if action == '4':
            break  # 결제로 진행

    # 주문이 하나도 없는 경우 다시 처음으로
    if not orders:
        continue

    # 결제 진행
    total_price = ifp.funtion.check_out(orders)
    if total_price == 0:
        print("주문이 없습니다. 처음으로 돌아갑니다.\n")
        continue

    name = ifp.funtion.member_ship(ifp.var.point_list, total_price)

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ifp.var.all_orders.append({
        'timestamp': now,
        'orders': orders.copy(),
        'total_price': total_price
    })

    print(f"\n{name}님, 주문 감사합니다! 또 오세요.")
    print("=" * 45)
