---
title: 'Bilder und Videos'
---

It's possible to include images and videos.

These can be either static files in the project or included form an external
server.

A static file can be included liek this:
![Description of the image](/adam.jpg "Image Title")
In this case the image file is in the _static subfolder of the root of the
project

It's also possible to use localizzed version of the images:
![Union Jack](/flag.png "British Falg loaded from en/_static")
These files are in the _static subfolder of each language.

It's also possible to reference images in subfolders:.
![A math problem](/subfolder/math.jpeg "Example image loaded from a subfolder")

It's also possible to have no image title.
![A math problem](/subfolder/math.jpeg)

If the folder structure of the static files mirrors the content folder structure,
it's possible to omit the path to the image:
![Logo of the TU Berlin from _static](TU_Logo_kurz.png)
This also works for localized files:
![Logo of the TU Berlin from en/_static](TU_Logo.png)

Of course it's also possible to have linked images.
[![Logo of the TU Berlin from en/_static](TU_Logo.png)](https://www.tu-berlin.de "Homepage of the TU Berlin")

External pictures - that means, pictures stored on external servers - can be included in the same way:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed diam erat, ultricies in sem et, volutpat dapibus tellus. Nulla sollicitudin scelerisque velit vitae sagittis. Praesent luctus est lectus, eget suscipit metus mattis sit amet. Aenean augue erat, rutrum nec sollicitudin sed, tristique id odio. Pellentesque cursus leo vel massa scelerisque fringilla. Pellentesque ultrices viverra tristique. Duis risus mi, vestibulum et molestie ut, elementum et leo. Quisque tortor lorem, mollis sit amet eros et, placerat egestas ligula. Duis at augue ipsum. Aenean sit amet pretium elit. Vivamus non metus convallis, auctor ipsum vitae, gravida nulla. Praesent bibendum mauris a lorem congue tincidunt.
![external $\LaTeX$ *example* _file_](https://picsum.photos/200 "An **example** _picture_ $\LaTeX$ from an external server")
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed diam erat, ultricies in sem et, volutpat dapibus tellus. Nulla sollicitudin scelerisque velit vitae sagittis. Praesent luctus est lectus, eget suscipit metus mattis sit amet. Aenean augue erat, rutrum nec sollicitudin sed, tristique id odio. Pellentesque cursus leo vel massa scelerisque fringilla. Pellentesque ultrices viverra tristique. Duis risus mi, vestibulum et molestie ut, elementum et leo. Quisque tortor lorem, mollis sit amet eros et, placerat egestas ligula. Duis at augue ipsum. Aenean sit amet pretium elit. Vivamus non metus convallis, auctor ipsum vitae, gravida nulla. Praesent bibendum mauris a lorem congue tincidunt.
![external example file](https://picsum.photos/200 "An example picture from an external server")
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed diam erat, ultricies in sem et, volutpat dapibus tellus. Nulla sollicitudin scelerisque velit vitae sagittis. Praesent luctus est lectus, eget suscipit metus mattis sit amet. Aenean augue erat, rutrum nec sollicitudin sed, tristique id odio. Pellentesque cursus leo vel massa scelerisque fringilla. Pellentesque ultrices viverra tristique. Duis risus mi, vestibulum et molestie ut, elementum et leo. Quisque tortor lorem, mollis sit amet eros et, placerat egestas ligula. Duis at augue ipsum. Aenean sit amet pretium elit. Vivamus non metus convallis, auctor ipsum vitae, gravida nulla. Praesent bibendum mauris a lorem congue tincidunt.
![external example file](https://picsum.photos/200)
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed diam erat, ultricies in sem et, volutpat dapibus tellus. Nulla sollicitudin scelerisque velit vitae sagittis. Praesent luctus est lectus, eget suscipit metus mattis sit amet. Aenean augue erat, rutrum nec sollicitudin sed, tristique id odio. Pellentesque cursus leo vel massa scelerisque fringilla. Pellentesque ultrices viverra tristique. Duis risus mi, vestibulum et molestie ut, elementum et leo. Quisque tortor lorem, mollis sit amet eros et, placerat egestas ligula. Duis at augue ipsum. Aenean sit amet pretium elit. Vivamus non metus convallis, auctor ipsum vitae, gravida nulla. Praesent bibendum mauris a lorem congue tincidunt.
![](https://picsum.photos/200 "An example picture from an external server")
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed diam erat, ultricies in sem et, volutpat dapibus tellus. Nulla sollicitudin scelerisque velit vitae sagittis. Praesent luctus est lectus, eget suscipit metus mattis sit amet. Aenean augue erat, rutrum nec sollicitudin sed, tristique id odio. Pellentesque cursus leo vel massa scelerisque fringilla. Pellentesque ultrices viverra tristique. Duis risus mi, vestibulum et molestie ut, elementum et leo. Quisque tortor lorem, mollis sit amet eros et, placerat egestas ligula. Duis at augue ipsum. Aenean sit amet pretium elit. Vivamus non metus convallis, auctor ipsum vitae, gravida nulla. Praesent bibendum mauris a lorem congue tincidunt.
![](https://picsum.photos/200)
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed diam erat, ultricies in sem et, volutpat dapibus tellus. Nulla sollicitudin scelerisque velit vitae sagittis. Praesent luctus est lectus, eget suscipit metus mattis sit amet. Aenean augue erat, rutrum nec sollicitudin sed, tristique id odio. Pellentesque cursus leo vel massa scelerisque fringilla. Pellentesque ultrices viverra tristique. Duis risus mi, vestibulum et molestie ut, elementum et leo. Quisque tortor lorem, mollis sit amet eros et, placerat egestas ligula. Duis at augue ipsum. Aenean sit amet pretium elit. Vivamus non metus convallis, auctor ipsum vitae, gravida nulla. Praesent bibendum mauris a lorem congue tincidunt.

Vidos can be embedded in a similar way. When doing so, there are some details to keep in mind:
no "!" at the front of the statement, and it hast to have {.video .video-static} at the end
<<<<<<< HEAD
["L'Arrivee d'un train en gare de la Ciotat, 1895" from _static](/video.mp4){.video .video-static}
=======
["Test video" from _static](/video.mp4){.video .video-static}
>>>>>>> d17ad2d... fix video link

It can be done like this for images from external servers too:
["L'Arrivee d'un train en gare de la Ciotat, 1895" from  Wikipedia](https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv){.video .video-static}

Videos from youtube can be included in the same way. In this case we have to
have {.video .video-youtube} at the end of the statement.
[Wir sind TU Berlin - Weitersagen](https://www.youtube.com/watch?v=OlH6bqv5Z-c){.video .video-youtube}
