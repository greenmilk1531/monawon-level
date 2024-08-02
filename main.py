#made by green_milk
    with tab3:
        st.title("모나원 1주년을 축하합니다!")
        st.info("모나원은 지금? : 가지 3 단계")
        img = Image.open('monawon.png')
        st.image(img)
        e = st.number_input("년도", min_value=2000, max_value=2100, step=1)
        w = st.number_input("월", min_value=1, max_value=12, step=1)
        ee = st.number_input("일", min_value=1, max_value=31, step=1)
        g = st.number_input("개시글 수", step=1)
        d = st.number_input("댓글 수", step=1)
        b = st.number_input("방문 수", step=1)

        if st.button("조회하기"):
            # 입력한 날짜를 datetime 객체로 변환
            input_date = datetime(int(e), int(w), int(ee))
            # 현재 날짜
            current_date = datetime.now()
               
                # 날짜 차이 계산
            delta = current_date - input_date
                
                # 총 일수로부터 몇 달과 며칠이 지났는지 계산
            total_days = delta.days
            months = total_days // 30  # 간단히 30일을 한 달로 가정
            days = total_days % 30
            st.info(f"{months}개월 {days}일이 지났습니다.")
            days = total_days / 7
            if days >= 16 and g >= 600 and d >= 1000 and b >= 2000 :
                st.success("당신은 너구리 입니다!")
                
            elif days >= 12 and g >= 300 and d >= 500 and b >= 1000:
                st.success("당신은 라쿤 입니다!")

            elif days >= 8 and g >= 100 and d >= 300 and b >= 500:
                st.success("당신은 거위 입니다!")

            elif days >= 4 and g >= 50 and d >= 100 and b >= 300:
                st.success("당신은 뱁새 입니다!")

            elif days >= 0 and g >= 0 and d >= 1 and b >= 0:
                st.success("당신은 미어켓 입니다!")

            else:
                st.success("당신은 알 입니다!")
