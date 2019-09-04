/*
axios를 활용하여
https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1에 요청을 보내
1등 번호 6개가 담긴 winner 배열을 만들어 출력하세요.
*/

import axios from 'axios';
    componentDidMount = () => {
        axios.get (
            'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
        )
        .then((response) => {
            let winner = []
        for (i=0, i<=6, i++) {
            
        }
            console.log()
        }
    )
    
}