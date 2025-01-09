# keys()
# syntax- dicobj.keys()
# only give the values under the key 
d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
for i in d.values():
    print(i)

# items() 
# give the key and value pair in the output
d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
for i,j in d.items():
    print(i,j)

# get
d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
x=d.get("subject")
print(x)

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
print(d.values())

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
print(d.keys())

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
print(d.items())

# remove 
# pop
# syntax - dictobj.pop(key)
d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
d.pop()
print(d)

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
print(d.pop("fees"))
print(d)

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
d["name"].pop()
print(d)

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
d["subject"].pop(1)
print(d)

# clear()
d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
d.clear()
print(d)

# update 
# syntax -- dictobj.update(dictionary)
d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
d.update({"city":["ind","bpl","gwl"]})
print(d)

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
d.update(city=["ind","bpl","gwl"])
print(d)

# tuple
t=(10,20)
print(list(t))

#dict()
d=dict(name=["abc","def"],subject=["da","ds"])
print(d)

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
d.pop("name")
print(d)

d={"name":["abc","pqr","def"],"subject":["da","ds","java"],"fees":[1000,2000,3000]}
d.popitem()
print(d)
