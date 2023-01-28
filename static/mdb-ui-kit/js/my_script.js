function hideFlash() {

      var el = document.getElementById('alert');


      if ( el.style.display != 'none' ) {
      el.style.display = 'none';
      }
      else if(el.style.display != 'block'){
      el.style.display = 'block';
      }
    }
    
function showMenu() {

      var el = document.getElementById('hide-div');


      if ( el.style.display == 'none' ) {
      el.style.display = 'flex';
      }
      else {
      el.style.display = 'none';
      }
    }