const axios = require('axios')

// const text = 'this is a msg'
const url = `https://api.telegram.org/sendMessage?chat_id=62853775
3&text=인간시대의끝이도래했다`

axios.get(url)
    .then(res => {
        console.log(res)
    })