import rpyc
from constRPYC import *

conn = rpyc.connect(SERVER, PORT)  # Connect to the server

print("Initial list:", conn.root.exposed_value())

conn.root.exposed_append("banana")
conn.root.exposed_append("apple")
print("After append:", conn.root.exposed_value())

print("Size:", conn.root.exposed_size())
print("Contains 'apple'?", conn.root.exposed_contains("apple"))

print("Removing 'apple':", conn.root.exposed_remove("apple"))
print("After remove:", conn.root.exposed_value())

print("Clearing list:", conn.root.exposed_clear())
print("Final list:", conn.root.exposed_value())
