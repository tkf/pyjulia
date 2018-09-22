import PyCall

# Initialize julia.Julia once so that subsequent calls of julia.Julia()
# uses pre-configured DLL.
PyCall.pyimport("julia")[:Julia](init_julia=false)

let code = PyCall.pyimport("julia.pseudo_python_cli")[:main](ARGS)
    if code isa Integer
        exit(code)
    end
end
