# The boss wants one file per student. The copy-paste way:

resource "local_file" "alice" {
  filename = "alice.txt"
  content  = "Hello, alice!\n"
}

resource "local_file" "bob" {
  filename = "bob.txt"
  content  = "Hello, bob!\n"
}

resource "local_file" "carol" {
  filename = "carol.txt"
  content  = "Hello, carol!\n"
}
