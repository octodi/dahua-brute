{ pkgs ? import <nixpkgs> {} 
}:                                                                
pkgs.mkShell {
  name="dev-environment";
  buildInputs = [
    pkgs.python3                                                        
    pkgs.python3Packages.requests
  ];                                                                    
  shellHook = ''
    echo "Start developing..."                                          
  '';                                                                   
} 
