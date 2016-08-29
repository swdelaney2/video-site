$( document ).ready(function() {
    $(".individual_video").each(function(i){
      $(this).delay(500 * i).fadeIn(500);
    })

    $(".individual_video").hover(function(){
      $(".individual_video").css("background", "rgb(255, 255, 255)")
      $(this).css("background", "rgb(68, 68, 68)")
      $(this).find("h1").css("text-decoration", "underline")
      description_text = $(this).find(".description").html();
      $(".moreinfo-sidebar").html("No description.")
      $(".moreinfo-sidebar").html(description_text)
    })

    $(".individual_video").mouseleave(function(){
      $(".individual_video").css("background", "rgb(255, 255, 255)")
      $(".moreinfo-sidebar").html("Hover over any video for more information!")
      $("h1").css("text-decoration", "none")
    })
});
