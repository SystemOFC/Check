page_content = '''
<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>CHECKUSER</title>

    <style>
        @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,100,500,700,900);

        html,
        body {
            margin: 0;
            padding: 0;
            font-family: 'Roboto', sans-serif;
        }

        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100vw;
            background: url(https://i.postimg.cc/Ghk1dPYr/dark-background-abstract-background-network-3d-background-7680x4320-8324.png);
            background-size: cover;
        }

        .container {
            margin: 1rem;
            border-radius: 50px;
            border: none;
            background: rgb(39, 39, 39);
            width: 300px;
            padding: 30px;
        }

        .detailsArea {
            display: flex;
            flex-direction: column;
        }

        .detailsArea label,
        .search label {
            color: white;
            margin-left: 5px;
            margin-bottom: 5px;
            font-size: 1rem;
        }

        .detailsArea input,
        .search input {
            font-size: 1rem;
            padding: 10px;
            border: none;
            border-radius: 50px;
            outline: 0;
            background: #212125;
            margin-bottom: 10px;
            color: #f0f0f0;
        }

        .search {
            display: flex;
            flex-direction: column;
            margin-bottom: 50px;
        }

        .container h1 {
            color: white;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }

        .container h4 {
            color: white;
            font-size: 1rem;
            margin-bottom: 20px;
        }

        .container h4 span {
            background: #363636;
            padding: 5px;
            border-radius: 50px;
            font-size: 0.8rem;
        }
    </style>

</head>

<body>
    <div class="container">
        <h1>&emsp;&ensp;LTECH CHECKUSER</h1>
<br>
        <div class="search">
            <label for="search">=x=x=x=x=BUSCAR USUÁRIO=x=x=x=x=</label>
            <input type="text" id="search" placeholder="">
        </div>
        <div class="detailsArea">
            <label for="username">NOME DE USUÁRIO</label>
            <input type="text" id="username" name="username" readonly />
        </div>
        <div class="detailsArea">
            <label for="limit">LIMITE DE CONEXÕES</label>
            <input type="text" id="limit" name="limit" readonly />
        </div>
        <div class="detailsArea">
            <label for="current">TOTAL DE CONEXÕES</label>
            <input type="text" id="current" name="current" readonly />
        </div>
        <div class="detailsArea">
            <label for="expires">DATA DE EXPIRAÇÃO</label>
            <input type="text" id="expires" name="expires" readonly />
    </div>

    <script src="https://code.jquery.com/jquery-3.6.1.min.js"
        integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ=" crossorigin="anonymous"></script>
    <script src="https://cdn.socket.io/4.5.3/socket.io.min.js"
        integrity="sha384-WPFUvHkB1aHA5TDSZi6xtDgkF0wXJcIIxXhC6h8OT8EH3fC5PWro5pWJ1THjcfEi"
        crossorigin="anonymous"></script>
    <script type="text/javascript" charset="utf-8">
        $(document).ready(function () {
            const namespace = 'ws://w.dutra01.xyz:5000';
            // const namespace = 'ws://127.0.0.1:5000';
            const socket = io();
            socket.on('message', function (data) {
                data = JSON.parse(data);

                if (data.total != undefined) {
                    $('#total').text(data.total);
                    return;
                }

                cleanFields();

                if (!data.username)
                    return;

                $('#username').val(data.username);
                $('#limit').val(data.limit_connections);
                $('#current').val(data.count_connections);
                $('#expires').val(data.expiration_date + ' - ' + data.expiration_days + ' dias');
            });

            socket.emit('message', {
                action: 'all',
                data: null
            });

            function cleanFields() {
                $('#username').val('');
                $('#limit').val('');
                $('#current').val('');
                $('#expires').val('');
            }

            let timeout, delay = 500;
            $('#search').keyup(function (e) {
                clearTimeout(timeout);
                timeout = setTimeout(function () {
                    socket.emit('message', {
                        action: 'check',
                        data: {
                            username: $('#search').val()
                        }
                    });
                }, delay);
            });
        });
    </script>
</body>

</html>
'''
