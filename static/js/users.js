var $window = $(window)
    	var $body   = $(document.body)

    	var navHeight = $('.navbar').outerHeight(true) + 10


	   setTimeout(function () {
      var $sideBar = $('.side-bar')

      $sideBar.affix({
        offset: {
          top:0
        , bottom: 80
        }
      })
    }, 100)