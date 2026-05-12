// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Pairings {
    // bilinear pairing demo using the bn128 ecPairing precompile (0x08)

    error PrecompileCallFailed();
    error PairingCheckFailed();
    error InvalidInputLength();

    function run(uint256[12] memory input) public view {
        bool success;
        bool ok;

        // 0x0180 = 384 bytes of input = 2 pairs of (G1, G2)
        assembly {
            success := staticcall(gas(), 0x08, input, 0x0180, 0x00, 0x20)
            ok := mload(0x00)
        }
        if (!success) revert PrecompileCallFailed();
        if (!ok) revert PairingCheckFailed();
    }

    // alternative implementation using bytes instead of fixed-size array
    function run(bytes calldata input) public view {
        if (input.length % 192 != 0) revert InvalidInputLength();
        (bool success, bytes memory data) = address(0x08).staticcall(input);
        if (!success) revert PrecompileCallFailed();
        if (!abi.decode(data, (bool))) revert PairingCheckFailed();
    }
}
