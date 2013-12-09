

## Encrypt and publish messages for a specific user

```shell
hubcrypt --publish rgbkrk -m "this is the secret"
```

## Use a specific key from the GitHub API

```json
[
  {
    "id": 6089446,
    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDRkGTt3IW4snceuvep4scqRPx1IHPd7pRblLb611mcBb5Yo12jjp6vnyEhvxrSY85HVDXK4q7voeG1zTwAmeD7iJ2WeXi5a42UclVBcTxG1QePrFvv9NcZlNz39J9utfs8Hf+RPbMpa0FWw9+0Q9X8SPaQkmUQKnlBm29lYS7S/DWfowF0vu6jOaFJHECIgSA4WbudjVQyDTNvzcffdocMc1z5YaGSDuslK7OafZA1aDRWghU1vNUcP2ZN0h3JfGt56WauukJU19ZNuuIl25EgPuPTFLlq11Agp3p5cVpfo+Fym9ghCzzavxPKfeqGjrxq/dwBxH9MN85g3dSAM8b3"
  },
  {
    "id": 6272418,
    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYoqGyixCqMPldcF+L+3G9XVRDnEu6zgJP2UZuKlqrzsMkS7uSZZbS8PfV3KtfRyP23FzePNmHQR5/BDoxPYFVf4evppTMZVgGY4Pu+V+NtVh8YRNH5+2ZAR1kEelqF25y02Xnf69xEO1p/aovMoHP6/h8TBjpj2RNndE3efYtwSITvOFsBoZXDtuuFy1zUh7atDnfhEvkKRsR0NeOGcSHJSyMpGO33wnbhE/1ZjQW3iv+RwBM4YpLewOUCGenMUoFQl3589yGofP08FCToPocpEzXdF812zh39116moMTISlTkRuxcYI0X2NMgvREIypl1oW3Ziqs+V1M+BAPqUAx"
  }
]
```

```shell
hubcrypt rgbkrk -m "Test" --id=6089446
```

## Set up reading spec

```shell
hubcrypt --read
```

## Use a setup/config?


