
// 确保 DOM 加载完毕
document.addEventListener('DOMContentLoaded', function () {

    // 设置查询按键事件的监听
    document.getElementById('query-student').addEventListener('click', function () {
        // 预处理url
        var baseUrl = 'http://127.0.0.1:5000/student/';
        var studentId = document.getElementById('student-id').value;
        var url = baseUrl + studentId;

        // 发送 fetch 请求
        fetch(url, {
            method: 'GET',
        })
            .then(response => response.text()) // 服务器返回 HTML
            .then(data => console.log(data))
            .catch((error) => console.error('Error:', error));
    });

    // 设置录入按键事件的监听
    document.getElementById('add-student').addEventListener('click', function () {
        var url = 'http://127.0.0.1:5000/student/new';
        var studentId = document.getElementById('student-id').value;
        var studentName = document.getElementById('student-name').value;
        var studentRegisterYear = document.getElementById('student_register_year').value;
        var csrfToken = document.getElementById('csrf_token').value;
        // 发送 fetch 请求
        fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                id: studentId,
                name: studentName,
                register_year: studentRegisterYear
            })
        })
            .then(response => response.text()) // 服务器返回 HTML
            .then(data => console.log(data))
            .catch((error) => console.error('Error:', error));
    });


    // 学生入学年份选择器
    // 获取当前年份
    var currentYear = new Date().getFullYear();

    // 创建一个 select 元素
    var select = document.createElement('select');
    select.id = 'student_register_year';
    select.name = 'year';

    // 生成从 1900 年到当前年份的所有 option 元素
    for (var year = 1900; year <= currentYear; year++) {
        var option = document.createElement('option');
        option.value = year;
        option.text = year;
        select.appendChild(option);
    }

    // 获取 div 元素
    var div = document.getElementById('student-content');

    // 将 select 元素添加到 div 元素中
    div.appendChild(select);
});
