# Tx_pool_monitor
A tool that allows you to query the ethereum TX pool.

## requirement files to be placed in root directory
* test_acc.json (ethereum address keystore file)
* test_acc.pass (password to keystore file)

## setup




update submodules
```
cd tx_pool_monitor
git submodule update --init --recursive
```
install requirements inside of submodules and create `_virtualenv` file
```
./install.sh
```
run the program
```
./start.sh
```

