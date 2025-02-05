{
  description = "Flake to manage Dark Matter grub themes from Vandal";

  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixpkgs-unstable;

    flake-compat = {
      url = "github:edolstra/flake-compat";
      flake = false;
    };
  };

  outputs = { self, nixpkgs, flake-compat }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    with nixpkgs.lib;
    {
      nixosModule = { config, ... }:
        let
          cfg = config.boot.loader.grub.darkmatter-theme;

          darkmatter-grub-theme = pkgs.stdenv.mkDerivation {
            name = "darkmatter-grub-theme";
            src = ./.;
            installPhase = ''
              mkdir -p $out/grub/theme/
              
              cp assets/backgrounds/${cfg.style}-${cfg.resolution}.png $out/grub/theme/background.png
              cp -r assets/icons-${cfg.resolution}/${cfg.icon}/ $out/grub/theme/icons/
              cp -r assets/fonts/${cfg.resolution}/* $out/grub/theme/
              cp -r base/${cfg.resolution}/* $out/grub/theme
            '';
          };
        in
        {
          options = {
            boot.loader.grub.darkmatter-theme = {
              enable = mkOption {
                type = types.bool;
                default = false;
                example = true;
                description = ''
                  Enable Dark Matter grub theme from Vandal
                '';
              };
              style = mkOption {
                type = types.enum [
                  "arch"
                  "archstrike"
                  "artix"
                  "avix"
                  "blackarch"
                  "centos"
                  "chromeos"
                  "debian"
                  "deepin"
                  "devuan"
                  "elementary"
                  "endeavouros"
                  "fedora"
                  "freebsd"
                  "garuda"
                  "gentoo"
                  "kali"
                  "kdeneon"
                  "kubuntu"
                  "linux"
                  "linuxlite"
                  "linuxmint"
                  "lubuntu"
                  "manjaro"
                  "mx"
                  "opensuse"
                  "parrot"
                  "pentoo"
                  "popos"
                  "redhat"
                  "slackware"
                  "solus"
                  "sparky"
                  "steamos"
                  "ubuntu"
                  "ubuntumate"
                  "void"
                  "windows10"
                  "windows11"
                  "zorin"
                  "guixsd"
                  "nixos"
                  "xubuntu"
                  "dtos"
                  "nobara"
                ];
                example = "nixos";
                description = ''
                  The theme to use for grub
                '';
              };
              icon = mkOption {
                type = types.enum [ "color" "white" ];
                default = "color";
                example = "color";
              };
              resolution = mkOption {
                type = types.enum [ "1080p" "1440p" ];
                default = "1080p";
                example = "1080p";
              };

            };
          };

          config = mkIf cfg.enable (mkMerge [{
            environment.systemPackages = [ darkmatter-grub-theme ];
            boot.loader.grub = {
              theme = "${darkmatter-grub-theme}/grub/theme";
            };
          }]);
        };
    };
}
