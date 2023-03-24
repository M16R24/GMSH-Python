import gmsh
import sys

gmsh.initialize(sys.argv)

gmsh.model.add("Slab2D")

lc = 1e-02
p1 = gmsh.model.geo.add_point(0, 0, 0, lc)
p2 = gmsh.model.geo.add_point(0, 1, 0, lc)
p3 = gmsh.model.geo.add_point(1, 1, 0, lc)
p4 = gmsh.model.geo.add_point(1, 0, 0, lc)

l1 = gmsh.model.geo.add_line(p1, p2)
l2 = gmsh.model.geo.add_line(p2, p3)
l3 = gmsh.model.geo.add_line(p3, -p4)
l4 = gmsh.model.geo.add_line(p4, -p1)

f1 = gmsh.model.geo.add_curve_loop([l1, l2, l3, l4])

s1 = gmsh.model.geo.add_plane_surface([f1], 1)

h = 0.1
gmsh.model.geo.extrude([(2, s1)], 0, 0, h, [1, 1], [1, 1], True)

s = gmsh.model.getEntities()

gmsh.model.geo.synchronize()

gmsh.model.mesh.set_transfinite_curve(l1, 21)
gmsh.model.mesh.set_transfinite_curve(l2, 21)
gmsh.model.mesh.set_transfinite_curve(l3, 21)
gmsh.model.mesh.set_transfinite_curve(l4, 21)

gmsh.model.mesh.set_transfinite_surface(s1)
gmsh.model.mesh.recombine()

gmsh.model.mesh.generate()

gmsh.write("slab.msh")

gmsh.option.set_number("Geometry.PointNumbers", 1)
gmsh.option.set_color("Mesh.Color.Points", 255, 0, 0)

r, g, b, a = gmsh.option.getColor("Geometry.Points")
gmsh.option.setColor("Geometry.Surfaces", r, g, b, a)


if 'close' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()