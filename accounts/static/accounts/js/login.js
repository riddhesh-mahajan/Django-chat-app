$('#login_btn').click(() => {
    $.ajax({
        url: login_api_url,
        type: 'POST',
        data: {
            email: $('#email').val(),
            password: $('#password').val(),
        },
        dataType: 'json',
        success(json) {

            if (json.error_flag !== undefined && json.error_flag === 0) {
                // Process msg and data
                switch (json.msg) {
                    case 'log in successful':
                        Cookies.set('email', $('#email').val())
                        window.open(chat_page_url, '_self');
                        break;
                    default:
                }
            } else {
                // Error occured
                switch (json.error) {
                    case 'login failed':

                        break;

                    case 'invalid parameters':

                        break;

                    default:

                }
            }
        },
    });
});

