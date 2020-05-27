const chat_holder_div = $('#chat_holder');
let socket = null;

setup_websocket();

function append_chat_card_in_chat_holder(msg, email) {
    let ml_auto_css_class = '';
    if (email === Cookies.get('email')) {
        ml_auto_css_class = 'ml-auto';
    }

    chat_holder_div.append(`
    <div class="d-flex mt-3">
        <div class="d-flex flex-column br1 shadow-sm border p-2 pr-3 pl-3 ${ml_auto_css_class}"
            style="min-width:30%;max-width:70%;">

            <p class="f4 mb-0">${msg}</p>
        </div>
    </div>
  `);
}

function setup_websocket() {
    const loc = window.location;
    let ws_start = 'ws://';
    if (loc.protocol === 'https:') {
        ws_start = 'wss://';
    }
    const endpoint = `${ws_start + loc.host}/chat-api/`;

    // This variable will be global, so it can be accessed from any js function
    socket = new ReconnectingWebSocket(endpoint);

    // On message received
    socket.onmessage = (e) => {
        const response = JSON.parse(e.data);
        const msg = response.msg;
        const email = response.email;
        if (email !== Cookies.get('email')) {
            append_chat_card_in_chat_holder(msg, email);
        }
    };

    // On socket open
    socket.onopen = (e) => {
        window.setTimeout(() => {
            send_meesage('Hello')
        }, 5000);
    };

    // On error
    socket.onerror = (e) => {
    };

    // On socket closed
    socket.onclose = (e) => {
    };
}

function send_meesage(msg_value) {
    const data = {
        email: Cookies.get('email'),
        msg: msg_value,
    };

    socket.send(JSON.stringify(data));

    append_chat_card_in_chat_holder(msg_value, Cookies.get('email'));

    $('#chat_input').val('');
}

$('#send_btn').on('click', () => {
    const msg_value = $('#chat_input').val();

    send_meesage(msg_value);
});
