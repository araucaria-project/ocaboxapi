## Example usage

from ocaboxapi import Observatory

observatory = Observatory()

observatory.connect('alpaca')

luke = observatory.telescopes['ls']

luke.mount.slewtocoordinates(11.4, -52.239)
luke.mount.park()