<html>
    <head>
        <title>Trips</title>
    </head>
    <body>
        <h1>{{username}}'s Trips</h1>
        <table cellspacing="10"">
            <tr>
                <th>Trip ID</th>
                <th>Date</th>
                <th>Destination</th>
                <th>Miles</th>
                <th>Gallons</th>
            </tr>
            %for row in rows:
                <tr>
                    %for col in row:
                        <td>{{col}}</td>
                    %end
                </tr>
            %end
        </table>
        <p><a href="/menu">Return to menu</a></p>
    </body>
</html>