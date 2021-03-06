//  登录
$(function () {
    $('.login_btn').click(function () {
        var username = $('input[name="username"]').val();
        var password = $('input[name="password"]').val();
        $.ajax({
            url: '/login/',
            type: 'POST',
            dataType: 'json',
            data: {
                'username': username,
                'password': password,
                "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val(),
            },
            success: function (json) {
                console.log(json);
                if (json.token ) {
                    sessionStorage.clear();
                    localStorage.clear();
                    localStorage.token = json.token;
                    localStorage.username = json.username;
                    localStorage.user_id = json.id;
                    location.href = '/';
                }
            }
        });
    });
});

// 注册
$(function () {
    $('.register').click(function () {
        var username = $('#username').val();
        var password = $('#password').val();
        var pwd2 = $('#pwd2').val();
        $.ajax({
            url: '/register.html/',
            type: 'POST',
            dataType: 'json',
            data: {
                'username': username,
                'password': password,
                'pwd2': pwd2,
            },
            success: function (json) {
                console.log(json);
                if (json.code === 1000) {
                    location.href = '/login.html/';
                }else {
                    $('span.error').html('');
                    $.each(json, function (field, value) {
                        console.log(field, value);
                        $('#' + field).next().html(value[0]);
                    });
                    if (json.non_field_errors){
                        $('#pwd2').next().html(json.non_field_errors);
                    }
                }
            }
        });
    });
});


// 登录注册切换
$(function () {
    $("#login").click(function () {
        $("#login").css('display', 'none');
        $("#logout").css('display', 'block');
    });

    $('#logout').click(function () {
        $('#logout').css('display', 'none');
        $('#login').css('display', 'block');
    });
});

// 发表评论
$(function () {
    $('.comment-btn').click(function () {
        var content = $('textarea[id="id_comment"]').val();
        var article_id = $('#article_id').text();
        var pid = '';
        var comment_id = $('#comment_id').text();
        $.ajax({
            url: '/comments/',
            type: 'POST',
            data: {
                'article_id': article_id,
                'content': content,
                'pid': pid,
                'comment_id': comment_id,
                "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val(),
            },
            success: function (data) {
                console.log(data);
                var created_time = data.created_time;
                var content = data.content;
                var username = data.username;
                var comment_id = data.comment_id;
                var s = `<li class="comment-item">
                            <span class="nickname">${username}</span>
                            <time class="submit-date">${created_time}</time>
                            <div class="text">${content}</div>
                            <span id="comment_id" style="display: none">${comment_id}</span>
                            <div class="delete"><button>删除</button></div>
                        </li>`;
                if (content && $.trim(content)) {
                    $('#tips').hide();
                    $('ul.comment-list').append(s);
                    $('textarea[id="id_comment"]').val('');
                    window.location.reload();
                } else {
                    $('#tips').show();
                    $('textarea[id="id_comment"]').val('');
                    // window.location.reload();
                }
            },
            error: function (data) {
                console.log(data);
            }
        });
    });
});

// 删除评论
$(function () {
    $('.delete').click(function () {
        var comment_id = $(this).prev().prev().text();
        $.ajax({
            url: '/comments/',
            type: 'delete',
            headers: {'X-CSRFToken': $.cookie('csrftoken')},
            data: {
                'comment_id': comment_id,
            },
            success: function (data) {
                console.log(data);
                window.location.reload();
            },
            error: function (data) {
                console.log(data);
            }
        });
    });
});
