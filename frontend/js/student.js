document.getElementById('myButton').addEventListener('click', function() {
    // 预处理url
    var baseUrl = 'http://localhost:5000/student/';
    var studentId = document.getElementById('studentIdInput').value;
    var url = baseUrl + studentId;
  
    // 发送 fetch 请求
    fetch(url, {
      method: 'GET',
    })
    .then(response => response.text()) // 服务器返回 HTML
    .then(data => console.log(data))
    .catch((error) => console.error('Error:', error));
  });