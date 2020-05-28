$('#signup_btn').click(() => {
    $.ajax({
        url: signup_api_url,
        type: 'POST',
        data: {
            first_name: $('#first_name').val(),
            last_name: $('#last_name').val(),
            email: $('#email').val(),
            password: $('#password').val(),
        },
        dataType: 'json',
        success(json) {

            if (json.error_flag !== undefined && json.error_flag === 0) {
                // Process msg and data
                switch (json.msg) {
                    case 'account created successfully':
                        window.open('/login', '_self');
                        break;
                    default:
                }
            } else {
                // Error occured
                switch (json.error) {
                    case 'account already exist':

                        break;

                    case 'invalid parameters':

                        break;

                    default:

                }
            }
        },
    });
});

