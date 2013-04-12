<!DOCTYPE html>
<html>
  <head>
    <title>Admin</title>
  </head>
  <body>
    <h2>{{ page.get('url') }}</h2>
    <pre>
      {{ page.get('content') }}
    </pre>
  </body>
</html>